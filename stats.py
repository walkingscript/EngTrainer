import sqlite3
import getpass

from settings import stats_file


class Statistics:
    def __init__(self):
        self.__username = getpass.getuser()
        self.__stats = {
            'right_answers': None,
            'wrong_answers': None,
            'total_answers': None,
            'right_percent': None
        }
        self.__init_db()

    def __init_db(self):
        self.conn = sqlite3.connect(stats_file)
        self.cursor = self.conn.cursor()
        self.__fill_db()

    def __fill_db(self):
        q = '''
        CREATE TABLE IF NOT EXISTS stats (
            username text primary key,
            right_answers_count int default 0,
            wrong_answers_count int default 0,
            total_answers_count int default 0,
            right_answers_percent double default 0.0
        );
        
        DROP TRIGGER IF EXISTS calc_stats;
        CREATE TRIGGER IF NOT EXISTS calc_stats 
        AFTER UPDATE OF right_answers_count, wrong_answers_count ON stats
        BEGIN
            UPDATE stats
            SET total_answers_count = 
                new.right_answers_count + new.wrong_answers_count
            WHERE username = old.username;
            UPDATE stats
            SET 
                right_answers_percent = CAST(new.right_answers_count AS DOUBLE) /
                                        CAST(total_answers_count AS DOUBLE) *
                                        CAST(100 AS DOUBLE)
            WHERE username = old.username;
        END; 
        '''
        self.cursor.executescript(q)
        self.__reg_user()

    def __reg_user(self):
        q1 = f'SELECT username FROM stats WHERE username = "{self.__username}"'
        self.cursor.execute(q1)
        if not self.cursor.fetchone():
            q2 = f'INSERT INTO stats(username) VALUES ("{self.__username}")'
            self.cursor.execute(q2)

    def get_username(self):
        return self.__username

    def add_right_answer(self):
        q = f'''
            UPDATE 
                stats
            SET 
                right_answers_count = right_answers_count + 1
            WHERE
                username = "{self.__username}";
            '''
        self.cursor.execute(q)

    def add_wrong_answer(self):
        q = f'''
            UPDATE 
                stats
            SET 
                wrong_answers_count = wrong_answers_count + 1
            WHERE
                username = "{self.__username}";
            '''
        self.cursor.execute(q)

    def get_stats(self) -> dict:
        q = f'''
        SELECT 
            right_answers_count, 
            wrong_answers_count, 
            total_answers_count, 
            ROUND(right_answers_percent, 2)
        FROM 
            stats 
        WHERE 
            username = "{self.__username}"'''
        self.cursor.execute(q)
        data = self.cursor.fetchone()
        for i, key in enumerate(self.__stats.keys()):
            self.__stats[key] = data[i]
        return self.__stats

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
# EngTrainer
The program that make you learn new words and to extend your leksikon.
The program help to learn by heart the words you'll add into data/vocabruary.txt file.

For run of this project you needs Python 3.9 interpreter and virtual environment.

Download Python you can here: https://www.python.org/

After that, you should to create virtual environment in the project folder.
To do this you can this way.
In console type "pip install -m venv ./venv".
Next the enviroment needs to activate.
There is a bit difference in command if you're using Linux or Windows.
For Linux:
    source venv\bin\activate
For Windows:
    venv\scripts\activate
    
After you activated the environment you should install require libraries.
Type "pip install -r requirements.txt".

After that. Type "python main.py". The project had runed. 

You can compile project by using next command:
    pyinstaller -F main.py --clean --noconsole

Good Luck!

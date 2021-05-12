# EngTrainer
The program that make you learn new words and to extend your leksikon.
The program help to learn by heart the words you'll add into data/vocabruary.txt file.

For run of this project you needs Python 3.9 interpreter and virtual environment.

Download Python you can here: https://www.python.org/

After that, you should to create virtual environment in the project folder.
You can do it this way. In console type next command: 

    pip install -m venv ./venv

The environment needs to be activated.
There is a bit of difference in command if you're using Linux or Windows.

For Linux OS it will be look so:

    source venv\bin\activate

For Windows so:

    venv\scripts\activate
    
When you activated the environment, you should install require libraries.
Type next command or follow the hints of yours IDE to do it: 
    
    pip install -r requirements.txt

Then type final command:
    
    python main.py

The project should be run.

You can compile project by using next command:

    pyinstaller -F main.py --clean --noconsole

Good Luck!

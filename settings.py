import os


stats_file = 'stats.db'
vocabulary_file_path = 'data' + os.sep + 'vocabulary.txt'

stylesheets = {
    'default': 'font: 14pt "Open Sans";',
    'right_answer': 'font: 14pt "Open Sans";background-color: lightgreen;',
    'wrong_answer' : 'font: 14pt "Open Sans";background-color: pink;',
}
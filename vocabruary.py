import re
import random
from functools import reduce

from loguru import logger


logger.add('logs/vocabruary.txt')


class Vocabruary:
    '''Stores words.
    Provides the set of methods for work with vocabruary.'''

    def __init__(self, filename):
        self.__data = {}
        self.filename = filename
        if filename:
            self.data_divider = re.compile('(.*)(?= -) - (.*)')
            self.__load_data_from_text_file()

    def get_translation(self, word: str, partial_search=True):
        '''Looks for translation of word that was passed in the parameter "word".
        If it'll not find any match then the function will look for 
        partial match if the partial_match param is set(by default is True).'''
        try:
            return self.__data[word]
        except KeyError:
            if partial_search:
                for key, value in self.__data.items():
                    if word in key:
                        return value

    def get_random_source_word(self):
        return random.choice(list(self.__data.keys()))

    def get_all_source_words(self):
        '''Returns all source words.'''
        return self.__data.keys()

    def get_all_translations(self):
        '''Returns all translations from vocabruary.'''
        return reduce(lambda a, b: a + b, self.__data.values())

    def get_random_pair(self):
        '''Returns random pair consist of source word and one of its translation.'''
        key = random.choice(list(self.__data.keys()))
        value = random.choice(self.__data[key])
        return (key, value)

    def __load_data_from_text_file(self):
        '''Reads the file where each line as that pattern:
        english word - русский перевод 1, русский перевод 2, ..., русский перевод N'''
        with open(self.filename, encoding='utf-8') as file:
            for i, line in enumerate(file.readlines()):
                try:
                    key, value = self.__parse_line(line)
                    self.__data[key] = value
                except ValueError as e:
                    logger.warning(f'Error on loading line {i}.\n{e}')

    def __parse_line(self, line: str):
        data = self.data_divider.findall(line)
        src_word = data[0][0]
        translate_list = data[0][1].split(',')
        translate_list = list(map(str.strip, translate_list))
        return (src_word, translate_list)

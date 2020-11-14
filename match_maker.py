import random
from typing import NamedTuple

from vocabruary import Vocabruary


class WordSet(NamedTuple):
    question: str      # word that need to be translated
    guesses: list[str] # list with answers
    right_answer: int  # index of the right answer in guesses


class MatchMaker:
    '''Choses the set of word from Vocabruary.
    The set consist of:
        question: 1 word, that needs to be translated
        guesses: list that consist from N variants of translation
        right_answer: index of list element where the right answer.'''

    def __init__(self, lang='en', guess_count=4):
        '''Param lang accepts only ru or en and determines from which
        language will be translating words. By default en.'''
        if lang == 'en':
            self.make_set = self.__make_set_from_en_to_ru
        elif lang == 'ru':
            self.make_set = self.__make_set_from_ru_to_en
        self.guess_count = guess_count
        self.vc = Vocabruary(filename='data\\vocabruary.txt')

    def is_english_verb(self, word: str):
        '''Returns True if english word is a verb'''
        if word.startswith('to '):
            return True

    def is_russian_verb(self, word: str):
        '''Returns True if russian word is a verb'''
        word_ending = ('ть', 'ться')
        if word.endswith(word_ending):
            return True

    def __make_set_from_en_to_ru(self):
        '''Creates the set of words for round.
        Set of the WordSet type.
        The word translates from english to russian.'''
        question = self.vc.get_random_source_word()
        possible_answers = self.vc.get_translation(question)
        wrong_answers = list(filter(lambda x: x not in possible_answers, 
                                    self.vc.get_all_translations()))
        if self.is_english_verb(question):
            wrong_answers = list(filter(self.is_russian_verb, wrong_answers))
        else:
            wrong_answers = list(filter(lambda x: not self.is_russian_verb(x),
                                        wrong_answers))
        answers_for_set = random.choices(wrong_answers, k=self.guess_count-1)
        right_answer = random.choice(possible_answers)
        answers_for_set.append(right_answer)
        random.shuffle(answers_for_set)
        right_answer = answers_for_set.index(right_answer)
        return WordSet(question=question,
                       guesses=answers_for_set,
                       right_answer=right_answer)

    def __make_set_from_ru_to_en(self):
        '''Creates the set of words for round.
        Set of the WordSet type.
        The word translates from russian to english.'''
        right_answer, question = self.vc.get_random_pair()
        wrong_answers = list(filter(lambda x: x != right_answer, 
                                    self.vc.get_all_source_words()))
        if self.is_russian_verb(question):
            wrong_answers = list(filter(self.is_english_verb, wrong_answers))
        else:
            wrong_answers = list(filter(lambda x: not self.is_english_verb(x),
                                        wrong_answers))
        answers_for_set = random.choices(wrong_answers, k=self.guess_count-1)
        answers_for_set.append(right_answer)
        random.shuffle(answers_for_set)
        right_answer = answers_for_set.index(right_answer)
        return WordSet(question=question,
                       guesses=answers_for_set,
                       right_answer=right_answer)    
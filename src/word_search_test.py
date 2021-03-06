import unittest
import word_search
from word_search import WordSearch

class WordSearchTests(unittest.TestCase):

    def setUp(self):
        self.word_search = WordSearch("puzzle.txt")

    def test_reading_words_from_text_file(self):
        self.assertEqual(self.word_search.words,['BONES', 'KHAN', 'KIRK', 'SCOTTY', 'SPOCK', 'SULU', 'UHURA'])

    def test_reading_puzzle_from_text_file(self):
        self.word_search_2 = WordSearch("puzzle_test.txt")
        self.assertEqual(self.word_search_2.puzzle, [['U','M','K','H'],['L','L','S','H'],
                                                    ['H','S','U','P'],['B','R','J','S']])

    def test_getting_first_letter_of_first_word(self):
        self.word_search.get_next_letter()
        self.assertEqual(self.word_search.current_letter,'B')
        

unittest.main()

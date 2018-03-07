import unittest
import word_search
from word_search import WordSearch

class WordSearchTests(unittest.TestCase):

    def setUp(self):
        self.word_search = WordSearch("puzzle.txt")

    def test_reading_words_from_text_file(self):
        self.assertEqual(self.word_search.words,['BONES', 'KHAN', 'KIRK', 'SCOTTY', 'SPOCK', 'SULU', 'UHURA'])

    def test_reading_puzzle_from_text_file(self):
        pass

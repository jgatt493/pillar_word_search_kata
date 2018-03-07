import unittest
import word_search
from word_search import WordSearch

class WordSearchTests(unittest.TestCase):

    def setUp(self):
        self.word_search = WordSearch()

    def testReadingWordsFromTextFile(self):
        self.assertEqual(self.word_search.words,['BONES', 'KHAN', 'KIRK', 'SCOTTY', 'SPOCK', 'SULU', 'UHURA'])

unittest.main()

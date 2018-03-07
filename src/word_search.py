class WordSearch:

    """A class containing the necessary methods to solve a word search.

    words: a list to hold the words to be found in the puzzle
    puzzle: a list to hold the puzzle. This list will simulate a matrix by containing
         a list of lists, with each indicie accessible via puzzle[x][y]"""

    def __init__(self):

            self.words = []
            self.puzzle = []
            self.read_words("puzzle.txt")

    """reads the first line of the file containing the words to be found,
        appends to self.words
        input: file to be read
        output: self.words"""
    def read_words(self, file):
        with open(file,"r") as f:
            for line in f.readlines(1):
                line = line.strip("\n")
                for word in line.split(","):
                    self.words.append(word)

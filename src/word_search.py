class WordSearch:

    """A class containing the necessary methods to solve a word search.
        input: Tales a puzzle in the form of a text file
        output: Returns a solution to the puzzle

        words: a list to hold the words to be found in the puzzle
        puzzle: a list to hold the puzzle. This list will simulate a matrix by containing
         a list of lists, with each indicie accessible via puzzle[x][y]"""

    def __init__(self, file):
            self.words = []
            self.puzzle = []
            self.read_words(file)

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


            for line in f.readlines():
                line = line.strip('\n')
                letter_array = []
                for letter in line.split(","):
                    letter_array.append(letter)
                self.puzzle.append(letter_array)

    def get_next_letter(self):
        self.current_letter = self.words[0][0]



        
        

"""Word Finder: finds random words from a dictionary.

"""

import random

class WordFinder:
    """class with method for words in a given file"""
    def __init__(self, path):
        self.path = open(path, "r")
        self.words = []
        
    def __repr__(self)
        return f"WordFinder path={path}, words={words}"

    def count_lines(self):
        """iterates thru each line and inserts into an array"""
        for line in self.path:
            self.words.append(line.strip())
        return f"{len(self.words)} words read "
    
    def random(self):
        """returns random word from given file"""
        length = len(self.words)
        return random.choice(self.words)

    
class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        """contains file path of parent class"""
        super().__init__(path)
        self.path = open(path, "r")

    def no_hashtags(self):
        """skips over lines with # and returns words in line"""
        for line in self.path:
            word = line.strip()
            if '#' not in word:
                self.words.append(word)
        return self.words


    


    



test_path = 'words.txt'
test = WordFinder(test_path)

test_path2 = 'complex.txt'
test2 = SpecialWordFinder(test_path2)

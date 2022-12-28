"""Word Finder: finds random words from a dictionary."""

import random
import requests

# path = open ("words.txt", "r")



class WordFinder:

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)
        
class SpecialWordFinder(WordFinder):
    """Wordfined but can be filtered"""

    def __init__(self, path):
        super().__init__(path)
    
    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]



class AnagramChecker:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.words = f.read().lower().split('\n')

    def is_valid_word(self, word):
        """Checks if the given word (ie. the word of the user) is a valid word."""
        return word in self.words

    def get_anagrams(self, word1):
        """ Find all anagrams for the given word."""
        anagrams = set()
        for word2 in self.words:
            if self.is_anagram(word1, word2):
                anagrams.add(word2)
        return anagrams

    @staticmethod
    def is_anagram(word1, word2):
        word1 = list(word1.lower().strip())
        word2 = list(word2.lower().strip())
        if word1 == word2 or len(word1) != len(word2):
            return False
        for letter in word1:
            if letter not in word2:
                return False
            word2.pop(word2.index(letter))
        return True

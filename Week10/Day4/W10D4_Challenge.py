import re
from gensim.parsing.preprocessing import remove_stopwords
from datetime import datetime


class Text:
    @classmethod
    def from_file(cls, file_path):
        """Returns a Text instance from file"""
        with open(file_path, 'r') as f:
            return Text(f.read())

    def __init__(self, string):
        self.text = string
        self.words = list(map(str.lower, filter(None, re.split(r'[^\w-]', self.text))))

    def get_frequency(self, word):
        """Returns the frequency of a word in the text"""
        return self.words.count(word)

    def get_unique_words(self):
        """Returns a list of all the unique words in the text."""
        return list(set(self.words))

    def most_common(self):
        """Returns the most common word in the text."""
        frequency = dict(map(lambda word: (word, self.get_frequency(word)), self.get_unique_words()))
        return max(frequency, key=frequency.get)

    def most_common_fast(self):
        """Returns the most common word in the text."""
        words = self.words.copy()
        frequency = {}
        while len(words) > 0:
            word = words[len(words)-1]
            frequency[word] = 0
            for index in range(len(words)-1, -1, -1):
                if words[index] == word:
                    frequency[word] += 1
                    words.pop(index)
        return max(frequency, key=frequency.get)

    def most_common_fastest(self):
        """Returns the most common word in the text."""
        frequency = {}
        for word in self.words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        return max(frequency, key=frequency.get)


class TextModification(Text):
    @classmethod
    def from_file(cls, file_path):
        """Returns a Text instance from file"""
        with open(file_path, 'r') as f:
            return TextModification(f.read())

    def no_punctuation(self):
        return re.sub("[,.!?()\\/\":;—]", "", self.text)

    def no_stopwords(self):
        """Returns the text without any english stop-words """
        return remove_stopwords(self.text)

    def no_special(self):
        """Returns the text without any special characters. """
        return re.sub(r"\W", "", self.text)


start_time = datetime.now()
print(Text.from_file("the_stranger.txt").most_common())
print(datetime.now() - start_time)
start_time = datetime.now()
print(Text.from_file("the_stranger.txt").most_common_fast())
print(datetime.now() - start_time)
start_time = datetime.now()
print(Text.from_file("the_stranger.txt").most_common_fastest())
print(datetime.now() - start_time)


# print(Text(TextModification.from_file("the_stranger.txt").no_stopwords()).most_common_fastest())
# print(TextModification.from_file("the_stranger.txt").no_special())


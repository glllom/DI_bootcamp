import re

def is_correct(word):
    """
    Checks if there are only letters, digits or space in word
    """
    return bool(re.fullmatch(r'[\w ]+', word))



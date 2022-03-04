import anagram_checker


def is_validate(word):
    if word == '' or len(word.split(' ')) > 1:
        return False
    for letter in word:
        if not letter.isalpha():
            return False
    return True


word = ""
while word != 'e':
    word = input("Input a word, or 'e' to exit: ").strip()
    if not is_validate(word):
        print("Invalid input!")
        continue
    print("Here are all anagrams:")
    print(*(anagram_checker.AnagramChecker('sowpods.txt').get_anagrams(word)), sep=', ')
    print()
print('Bye-bye')

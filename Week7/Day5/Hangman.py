import random
from functools import reduce

"""
prints hangman depending by score of mistakes
"""
def show_hangman(score):
    print("   +----------+")
    print("   |          |")
    print(f"   |          {'O' if score > 0 else ' '}")
    print(f"   |        {'/' if score > 2 else ' '}{'| |' if score > 1 else '   '}{chr(92) if score > 3 else ' '}")
    print(f"   |       {'^' if score > 2 else ' '} {'|_|' if score > 1 else '   '} {'^' if score > 3 else ' '}")
    print(f"   |        {'/' if score > 4 else ' '}   {chr(92) if score > 5 else ' '} ")
    print(f"   |       {'^' if score > 4 else ' '}     {'^' if score > 5 else ' '}")
    print(" =================")
    print()


"""
prints word with '*' and letters
"""
def show_word(word, used_letters):
    print('\u2554', *['\u2550' for _ in range(len(word) + 2)], '\u2557', sep='')  # border
    print('\u2551 ', end='')  # border
    for letter in word:
        print(letter if letter in used_letters else '*', end='')
    print(' \u2551')  # border
    print('\u255a', *['\u2550' for _ in range(len(word) + 2)], '\u255d', sep='')  # border


"""
checks if all word has been guessed
"""
def is_guessed(word, used_letters):
    return reduce((lambda bool1, bool2: bool1 and bool2), map(lambda letter: letter in used_letters, word))


"""
Check if user's choice is correct 
"""
def correct_choice(user_input, *args):
    if user_input not in args:
        print("Incorrect input.")
    return user_input in args


"""
Main function. Program starts from here.
"""
def main():
    choice = input("Would you like play the game (Y/N)? ").upper()
    while not correct_choice(choice, 'Y', 'N'):
        choice = input("Would you like play the game (Y/N)? ").upper()
    if choice == 'N':
        print('Bye-bye.')
        return
    #  player begins to play
    word = random.choice(wordslist)
    used_letters = set()
    score = 0
    show_hangman(score)
    while score < 6:
        show_word(word, used_letters)
        letter = input("Input a letter or <space>: ").lower()
        while not correct_choice(letter, *[chr(i) for i in range(97, 123)], ' '):
            letter = input("Input a letter or <space>: ").lower()

        if letter in used_letters:
            print("You already used this letter.")
            continue
        else:
            used_letters.add(letter)

        if letter in word:
            print('Correct!')
            if is_guessed(word, used_letters):
                print("Congratulations, you win!")
                show_word(word, used_letters)
                break
        else:
            print('Wrong!')
            score += 1
            show_hangman(score)
            print("You loose!" if score == 6 else f"Your score of mistakes: {score}")


# -------------------------------------------------------------------------------------------------------
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']
main()

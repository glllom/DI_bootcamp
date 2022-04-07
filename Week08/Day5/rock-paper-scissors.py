from game import Game
def get_user_menu_choice():
    choice = ""
    print("Menu:")
    while choice not in ['g', 'q', 's']:
        print("\t(g) PLay a new game")
        print("\t(s) Show scores")
        print("\t(q) Quit:\n\t")
        choice = input()
    return choice

def print_results(results):
    print("Game results:")
    for key, value in results.items():
        print(key, value, sep=': ')

def main():
    choice = get_user_menu_choice()
    new_game = Game()
    while choice != 'q':
        if choice == 'g':
            new_game.play()
        if choice == 's':
            try:
                print_results(new_game.get_results())
            except AttributeError:
                print("you don't have any score.")
        choice = get_user_menu_choice()
    print_results(new_game.get_results())
    print("Thank you for playing")


main()
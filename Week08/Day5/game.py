import random


class Game:
    def __init__(self):
        self.items = ["rock", "paper", "scissors"]
        self.results = {"win": 0, "loss": 0, "draw": 0}

    def get_user_item(self):
        item = input("Select item (rock/paper/scissors): ").strip()
        while item not in self.items:
            print("Wrong choice.")
            item = input("Select item (rock/paper/scissors): ").strip()
        return item

    def get_computer_item(self):
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        if self.items.index(user_item) - self.items.index(computer_item) in [1, -2]:
            return "win"
        else:
            return "loss"

    def play(self):
        users_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(users_item, computer_item)
        print(
            f'You selected {users_item}. The computer selected {computer_item}.'
            f' You {f"have a {result}" if result == "draw" else result}!')
        self.results[result] += 1
        return result

    def get_results(self):
        return self.results

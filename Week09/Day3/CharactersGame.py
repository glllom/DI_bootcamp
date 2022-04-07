class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other):
        other.life -= self.attack

    @staticmethod
    def turn_results(char1, char2):
        print(f"Result:\n\t{char1.name}'s life - {char1.life}\n\t{char2.name}'s life - {char2.life}")


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Wood whispers: Druid {self.name} has been created.")

    def meditate(self):
        self.attack -= 2
        self.life += 5
        print(f"{self.name} meditates. His life rises to {self.life} and attack power goes {self.attack}.")

    def animal_help(self):
        self.attack += 5
        print(f"{self.name} calls out to the animals. His attack power goes {self.attack}.")

    def fight(self, other_character):
        other_character.life -= 0.75 * (self.attack + self.life)
        print(f"{self.name} attacks to {other_character.name}")
        Character.turn_results(self, other_character)


class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Mountains yell: Warrior {self.name} was born!")

    def brawl(self, other_character):
        other_character.life -= 2 * self.attack
        self.life += 0.5 * self.attack
        print(f"{self.name} brawls with {other_character.name}")
        Character.turn_results(self, other_character)

    def train(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} trains. His life rises to {self.life} and attack power goes to {self.attack}.")

    def roar(self, other_character):
        other_character.attack -= 3
        print(
            f"{self.name} roars on {other_character.name}. {other_character.name}'s attack now {other_character.attack}")


class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Sky sings: Mage {self.name} comes in this world!")

    def curse(self, other_character):
        other_character.attack -= 2
        print(
            f"{self.name} curses at {other_character.name}. {other_character.name}'s attack now {other_character.attack}")

    def summon(self):
        self.attack += 3
        print(f"{self.name} summons the power of the spirit. His attack power rises to {self.attack}.")

    def cast_spell(self, other_character):
        other_character.life -= self.attack / self.life
        print(f"{self.name} casts spell on {other_character.name}")
        Character.turn_results(self, other_character)


# -------------------------------------------------------------------------


oaker = Druid('Oaker')
beaster = Warrior('Beaster', 25)
forcer = Mage('Forcer', 15, 15)

forcer.summon()
beaster.train()
oaker.fight(forcer)
beaster.roar(oaker)
forcer.curse(beaster)
forcer.summon()
forcer.cast_spell(beaster)

class Human:
    @staticmethod
    def validate(blood_type: str):
        return blood_type in ["A", "B", "AB", "O"]

    def __init__(self, id_number: str, name: str, age: int, prioritary: bool, blood_type: str):
        if not Human.validate(blood_type):
            raise ValueError("Invalid type of blood")

        self.id_number = id_number
        self.name = name
        self.age = age
        self.prioritary = prioritary
        self.blood_type = blood_type
        self.family = set()

    def add_family_member(self, person):
        """Adds the person to this human’s family and this human to the person’s family."""
        self.family.add(person)
        person.family.add(self)


class Queue:
    def __init__(self, list_humans=None):
        if not list_humans:
            self.list_humans = []
        else:
            self.list_humans = list_humans

    def add_person(self, person):
        """Add a human to the queue, if he is older than 60 years old or a prioritary person,\n'
            put him at the beginning of the list (at index 0) before every other."""
        if person.prioritary or person.age > 60:
            self.list_humans.insert(0, person)
        else:
            self.list_humans.append(person)

    def find_in_queue(self, person):
        """Returns the index of a human in the queue."""
        for index, p in enumerate(self.list_humans):
            if p == person:
                return index

    def swap(self, person1, person2):
        """Swaps person1 with person2."""
        index_1, index_2 = self.list_humans.index(person1), self.list_humans.index(person2)
        self.list_humans.append(self.list_humans.pop(index_1))
        self.list_humans.insert(index_1, self.list_humans.pop(index_2))
        self.list_humans.insert(index_2, self.list_humans.pop())

    def get_next(self):
        """return the next human in the queue, meaning the object at index 0 in the list."""
        if len(self.list_humans) == 0:
            return None
        return self.list_humans.pop(0)

    def get_next_blood_type(self, blood_type):
        """ Return the first human with this specific blood type."""
        if len(self.list_humans) == 0:
            return None
        for person in self.list_humans:
            if person.blood_type == blood_type:
                return self.list_humans.pop(self.list_humans(person))

    def sort_by_age(self):
        """Sort the queue so that the older ones are before the younger ones
         and all the prioritary persons are before the others."""
        self.list_humans.sort(reverse=True, key=lambda person: (person.prioritary, person.age))

    def print_queue(self):
        for index, person in enumerate(self.list_humans):
            print(index, ')', person.name, person.age, person.prioritary)

    def rearrange_queue(self):
        """method to the Queue class, so that there is no two members of the same family one after the other."""
        if len(self.list_humans) < 3:
            return
        for i in range(1, len(self.list_humans)):
            if self.list_humans[i] in self.list_humans[i-1].family:
                self.list_humans.append(self.list_humans.pop(i))
#  -----------------------------------------------------------------------------------------------------


h1 = Human("12341", "Leonard", 35, True, "B")
h2 = Human("12342", "Penny", 30, False, "A")
h3 = Human("12349", "Mary Cooper", 62, True, "O")
h4 = Human("12343", "Howard", 34, True, "B")
h5 = Human("12344", "Bernadette", 29, False, "AB")
h6 = Human("12348", "Beverly Hofstadter", 61, False, "B")
h7 = Human("12345", "Sheldon", 36, False, "O")
h8 = Human("12346", "Amy", 36, False, "O")
h9 = Human("12347", "Arthur Jeffries", 70, True, "A")

h1.add_family_member(h2)
h1.add_family_member(h6)
h3.add_family_member(h7)
h3.add_family_member(h8)
h7.add_family_member(h8)

q1 = Queue()
q1.add_person(h1)
q1.add_person(h2)
q1.add_person(h3)
q1.add_person(h4)
q1.add_person(h5)
q1.add_person(h6)
q1.add_person(h7)
q1.add_person(h8)
q1.add_person(h9)
q1.print_queue()
print('*********************')
q1.sort_by_age()
q1.print_queue()
print('*********************')
q1.rearrange_queue()
q1.print_queue()


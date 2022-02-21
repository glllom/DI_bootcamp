"""
Exercise 1 : Family
"""


class Family:
    members = []
    last_name = ""

    def __init__(self, name, age, gender, is_child):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_child = is_child
        self.members.append({'name': name,
                             'age': age,
                             'gender': gender,
                             'is_child': is_child})

    @classmethod
    def born(cls, **kwargs):
        kwargs['age'] = 0
        kwargs['is_child'] = True
        print("Congratulations with a new family member!")
        cls.members.append(kwargs)

    @classmethod
    def is_18(cls, name):
        for member in cls.members:
            if member['name'] == name:
                return member['age'] >= 18
        return f'There is no member with name {name}'

    @classmethod
    def print_family(cls):
        for member in cls.members:
            print(member)


michael = Family('Michael', 35, 'Male', False)
sarah = Family('Sarah', 32, 'Female', False)

Family.born(name='Nick', gender="Male")
print(Family.members)
print(Family.is_18('Sarah'))
print(Family.is_18('John'))
Family.print_family()
print(['*'*30])
print()
"""
Exercise 2 : The Incredibles Family
"""


class TheIncredibles(Family):
    last_name = "Parr"
    members = []

    def __init__(self, name, age, gender, is_child, incredible_name, power):
        super().__init__(name, age, gender, is_child)
        self.power = power
        self.incredible_name = incredible_name
        self.members[len(self.members)-1]['power'] = power
        self.members[len(self.members)-1]['incredible_name'] = incredible_name

    def use_power(self):
        if self.age >= 18:
            print(self.power)
        else:
            raise ValueError("Less than 18")

    @classmethod
    def incredible_presentation(cls):
        for member in cls.members:
            print(member['incredible_name'], member['power'], sep=' - ')


bob = TheIncredibles('Robert', 40, 'Male', False, 'Mr. Incredible', 'Superhuman strength')
helen = TheIncredibles('Helen', 35, 'Female', False, 'Elastigirl', 'Superhuman elasticity')
violet = TheIncredibles('Violet', 14, 'Female', True, 'Vi', 'Invisible, Force fields')
dash = TheIncredibles('Dashiel', 10, 'Male', True, 'Dash', 'Speedster')
jack = TheIncredibles('John Jackson', 1, 'Male', True, 'Jack-Jack', 'Multitude of superhuman abilities')

TheIncredibles.incredible_presentation()
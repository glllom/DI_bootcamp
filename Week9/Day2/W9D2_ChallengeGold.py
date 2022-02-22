persons = [tuple(input().split(',')) for _ in range(5)]
print(persons)
persons.sort(key=lambda person: (person[0], person[1], person[2]))
print(persons)

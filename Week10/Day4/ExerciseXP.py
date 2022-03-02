from random import choices
import json

"""Exercise 1 – Random Sentence Generator"""


def get_words_from_file():
    """This function reads the file’s content and return the words as a collection."""
    with open("sowpods.txt", "r") as f:
        return f.read().lower().split('\n')


def get_random_sentence(length):
    """This function takes a single parameter called 'length' and uses the words list to get random words."""
    words = (choices(get_words_from_file(), k=length))
    return f"{words[0].capitalize()} {' '.join(words[1::])}."


def main():
    print("Hi. This program generates a random sentence.")
    length = 0
    while length < 2 or length > 20:
        try:
            length = int(input("Please, enter the length of your random sentence (between 2 and 20): "))
        except ValueError:
            print('Invalid number')
            return
    print(get_random_sentence(length))


main()


"""Exercise 2: Working With JSON"""
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
person = json.loads(sampleJson)
print(f" Your salary is: ${person['company']['employee']['payable']['salary']}")
person['company']['employee']["birth_date"] = "01/01/1990"
with open("person.json", "w") as f:
    json.dump(person, f)

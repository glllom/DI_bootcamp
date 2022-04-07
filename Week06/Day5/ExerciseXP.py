"""
Exercise 1 : Convert Lists Into Dictionaries
"""

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)
#  --------------------------------------------------------------------------
"""
Exercise 2 : Cinemax #2
"""


def total_cost_calculator(family_dict):
    total_cost = 0
    for age in family_dict.values():
        if 3 <= int(age) <= 12:
            total_cost += 10
        if int(age) > 12:
            total_cost += 15
    return total_cost


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

print(f"Total price is {total_cost_calculator(family)}")

user_family = {}
print("\nPlease input all members of your family with ages.\nEvery member should be in new line.\nName of member "
      "and age please separate by comma.\nWhen you finish, input 'end' in new line.\n")

while True:
    member = input().split(",")
    if member == ["end"]:
        break
    if len(member) != 2:
        print("Incorrect input")
        continue
    if not member[1].strip().isdigit():
        print("Incorrect age")
        continue
    user_family[member[0]] = int(member[1].strip())
print("Your family is:")
print(*user_family)
print(f"Total price is {total_cost_calculator(user_family)}")

#  ----------------------------------------------------------------------------------------------------
"""
Exercise 3: Zara
"""
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H & M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print(f"clients of {brand['name']} are: {', '.join(brand['type_of_clothes'][:-1])}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print("Last international competitor is", brand["international_competitors"][-1])
print("Major colors in US are:", *brand["major_color"]["US"])
print(f"The are {len(brand)} keys:", *brand.keys(), sep='\n')

more_on_zara = {"creation_date": 1975, "number_stores": 10000}
brand.update(more_on_zara)
print(f"\nThe are {len(brand)} keys:", *brand.items(), sep='\n')
# -------------------------------------------------------------------------------------------------------------
"""
Exercise 4 : Disney Characters

"""
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#  1/
dict_disney = {}
for index, value in enumerate(users):
    dict_disney[value] = index
print(dict_disney)
#  2/
dict_disney = {}
for index, value in enumerate(users):
    dict_disney[index] = value
print(dict_disney)
#  3/
dict_disney = {}
for index, value in enumerate(sorted(users)):
    dict_disney[value] = index
print(dict_disney)


#  4.1/
def contains_i(word):
    return 'i' in word


dict_disney = {}
for index, value in enumerate(filter(contains_i, users)):
    dict_disney[value] = index
print(dict_disney)


#  4.2/
def start_mp(word):
    return word[0].lower() in ['m', 'p']


dict_disney = {}
for index, value in enumerate(filter(start_mp, users)):
    dict_disney[value] = index
print(dict_disney)

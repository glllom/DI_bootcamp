"""
Exercise 1 : Hello World-I Love Python
"""

print("Hello, World\n" * 4, "I love python\n" * 4, sep="")
# ------------------------------------------------------------------------------
'''
Exercise 2 : What Is The Season ?
'''
month = int(input("Give me number of month (1 to 12):"))
if month in [3, 4, 5]:
    print("Spring")
if month in [6, 7, 8]:
    print("Summer")
if month in [9, 10, 11]:
    print("Autumn")
if month in [12, 1, 2]:
    print("Winter")
# ------------------------------------------------------------------------------
"""
Exercise XP Ninja
"""
# ------------------------------------------------------------------------------
"""
Exercise 4 : How Many Characters In A Sentence ?
"""
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
          "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
          "Ut enim ad minim veniam, quis nostrud exercitation ullamco " \
          "laboris nisi ut aliquip ex ea commodo consequat. " \
          "Duis aute irure dolor in reprehenderit in voluptate velit " \
          "esse cillum dolore eu fugiat nulla pariatur. " \
          "Excepteur sint occaecat cupidatat non proident, " \
          "sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text.split(" ")))
# ------------------------------------------------------------------------------
"""
Exercise 5 : Longest Word Without A Specific Character?
"""
old_sentence = ""
new_sentence = input("Give me the longest sentence without 'a': ")
while "a" not in list(new_sentence) and "A" not in list(new_sentence):
    if len(old_sentence) > len(new_sentence):
        print(f"\"{old_sentence}\" is longer")
    else:
        print(f"Now \"{new_sentence}\" is the longest sentence.")
        old_sentence = new_sentence
    new_sentence = input("Give me the longest sentence without 'a': ")
print("Wrong sentence. Bye-bye.")  # when sentence contains "a"

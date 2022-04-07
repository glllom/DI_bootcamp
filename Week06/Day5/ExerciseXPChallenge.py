print("Hi. What you want do do? Enter 1 or 2.")
choice = int(input("1. Encryption\n2. Decryption\n: "))
shift = int(input("Enter shift (crypt-key): "))
if choice == 2:
    shift = -shift
message = input("Now enter your message: ")
#  alphabet in unicode from 97 to 123
new_message = "".join(chr((ord(letter) + shift - 97) % 26 + 97) for letter in message.lower())

print("After processing your message is:\n", new_message)


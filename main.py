

password = ""
a = ""
b = ""
def encode(password):
# encodes password of 8 digit length containing only integers
    encoded = ""
    if len(password) == 8:
        for i in password:
            encoded += str(int(i) + 3)
        return encoded

password = True
while password:
    option = 0
    option = int(input(f"Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option:"))
    if option == 1:
        password = input(f"Please enter your password to encode:")
        a = encode(password)
        print("Your password has been encoded and stored!")
    if option == 2:
        b = decode(a)
        print(f"The encoded password is {a}, and the original password is {b}.")
    if option == 3:
        # ends the program
        break

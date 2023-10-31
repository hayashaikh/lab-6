# added comment to code repository - Kassa
encoded_passwords={} #Added
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
#Kassahun edit, I made the decoder function
def Decoder(password):
    # string to store decoded password
    decoded_pass = ""

    # decoding of each digit
    for char in password:
        decoded_pass = decoded_pass + str((int(char) - 3) % 10)  # shiftng 3 digit

    # return decoded password
    return decoded_pass

password = True
while password:
    option = 0
    option = int(input(f"Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option:"))
    if option == 1:
        password = input(f"Please enter your password to encode:")
        a = encode(password)
        encoded_passwords[a]=password
        print("Your password has been encoded and stored!")
        #edit, Kassahun
        # I created the decoder if statements
    elif option == 2:
        a = input("Please enter the encoded password: ")
        if a in encoded_passwords:
            originalPass = encoded_passwords[a]
            print(f"The encoded password is {a}, and the original password is {originalPass}.")
        else:
            print("Password not found")
    elif option == 3:
        # ends the program
        break

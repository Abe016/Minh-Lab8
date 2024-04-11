# Minh Pham's main.py file

def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode(encoded_password):
    pass

if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print(f"Your password has been encoded and stored!")
            else:
                print("Password must be an 8-digit string containing only integers.")
        elif choice == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}")
            # encoded_password = input("Enter the encoded password: ")
            # if len(encoded_password) == 8 and encoded_password.isdigit():
            #     original_password = decode(encoded_password)
            #     print(f"Original password: {original_password}\n")
            # else:
            #     print("Invalid encoded password. Encoded password must be an 8-digit string containing only integers.")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
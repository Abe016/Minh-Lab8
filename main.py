# Minh Pham's main.py file

def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode(password):
    result = ""
    for x in str(password):
        if int(x) > 3:
            result += str(int(x) - 3)
        else:
            result += str(int(x) + 6)


    return int(result)

if __name__ == "__main__":
    while True:
        print("1. Encode password\n2. Decode password\n3. Exit\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            password = input("Enter an 8-digit password: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print(f"Encoded password: {encoded_password}\n")
            else:
                print("Invalid password. Password must be an 8-digit string containing only integers.")
        elif choice == 2:
            encoded_password = input("Enter the encoded password: ")
            if len(encoded_password) == 8 and encoded_password.isdigit():
                original_password = decode(encoded_password)
                print(f"Original password: {original_password}\n")
            else:
                print("Invalid encoded password. Encoded password must be an 8-digit string containing only integers.")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
def main():
    # Declare local variable for original and encoded password
    original_password = None
    encoded_password = None

    # While loop to keep the menu running
    while True:
        # Print user menu
        print_menu()
        # Prompt user to select menu option
        user_option = int(input('Please enter an option: '))

        # If user selects, option 1, prompt user to input a password to be encoded and assign encoded pass to variable
        if user_option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')

        # If user selects option 2, print encoded password and original password
        if user_option == 2:
            original_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {original_password}\n')

        # If the user selects option 3, break from loop and end program
        if user_option == 3:
            break


# Function to encode password, adds 3 to each digit in password and augments final string with that digit
def encode(raw_password):
    encoded = ''
    for i in raw_password:
        encoded += str((int(i) + 3) % 10)
    return encoded


# Function to decode password, subtracts 3 from each digit in password and augments final string with that digit
def decode(encoded_password):
    if not (encoded_password): return ""

    password : str = ""
    for num in encoded_password:
        password += str((int(num) - 3) % 10)
    return password


# Function to print user selection menu
def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit', end='\n\n')


# Starting point for program
if __name__ == '__main__':
    main()

import string

# Set the minimum and maximum length for the password
MIN_LENGTH = 6
MAX_LENGTH = 12

# Initialize a variable to keep track of the number of attempts
attempts = 0

# Keep prompting the user for a password until they enter a valid one
# or until they have made 5 attempts
while attempts < 5:
    # Prompt the user for a password
    password = input('Enter a password: ')

    # Check the length of the password
    if MIN_LENGTH <= len(password) <= MAX_LENGTH:
        # Initialize variables to keep track of the types of characters
        # that are present in the password
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False

        # Iterate over each character in the password
        for char in password:
            # Check if the character is a lowercase letter
            if char in string.ascii_lowercase:
                has_lower = True
            # Check if the character is an uppercase letter
            elif char in string.ascii_uppercase:
                has_upper = True
            # Check if the character is a digit
            elif char in string.digits:
                has_digit = True
            # Check if the character is a special character
            elif char in '$#@':
                has_special = True

        # Check if the password meets all of the criteria
        if has_lower and has_upper and has_digit and has_special:
            # The password is valid
            print('Valid password')
            break
        else:
            # The password is not valid
            print('Invalid password')
    else:
        # The password is not the correct length
        print('Invalid password')

    # Increment the number of attempts
    attempts += 1

# Inform the user that the authorities have been alerted
print('The authorities have been alerted')
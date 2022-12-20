import string
MIN_LENGTH = 6
MAX_LENGTH = 12
attempts = 0
while attempts < 5:
    password = input('Enter a password: ')
    if MIN_LENGTH <= len(password) <= MAX_LENGTH:
        #bool value for checking
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        for char in password:
            if char in string.ascii_lowercase: 
                has_lower = True
            elif char in string.ascii_uppercase:
                has_upper = True
            elif char in string.digits:
                has_digit = True
            elif char in '$#@':
                has_special = True
        if has_lower and has_upper and has_digit and has_special:
            # The password is valid
            print('Valid password')
            break
        else:
            print('Invalid password')
    else:
    
        print('Invalid password')
    # Increment the number of attempts
    attempts += 1
print('The authorities have been alerted')
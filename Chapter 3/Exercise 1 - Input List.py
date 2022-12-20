def name(firstname,lastname):
    firstname = firstname
    lastname = lastname
    print(f'Full Name: {firstname.title()} {lastname.title()}')

firstname = str(input("Input first name: "))
lastname = str(input("Input last name: "))

name(firstname,lastname)
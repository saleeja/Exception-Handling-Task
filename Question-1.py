"""Write a Python program that prompts the user to enter an integer and handles the ValueError exception if the user enters a non-integer value."""

def integer_input():
    while True:
        try:
            user_input = input("Enter an integer: ")
            user_integer = int(user_input)
            return user_integer 
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


user_integer = integer_input()

print("You entered:", user_integer)

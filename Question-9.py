"""9.Write a Python program that prompts the user to enter their age. Define a custom exception called InvalidAgeError that is raised when the entered age is less than 0 or greater than 150. Handle the InvalidAgeError exception and display an appropriate error message."""


class InvalidAgeError(Exception):
    pass


def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 150:
                raise InvalidAgeError("Age must be between 0 and 150")
            return age
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except InvalidAgeError as e:
            print(e)


try:
    age = get_age()
    print(f"Your age is: {age}")
except KeyboardInterrupt:
    print("\nProgram exited.")

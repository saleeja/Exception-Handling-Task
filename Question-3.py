"""3.Write a program that calculates the division of two numbers entered by the user. 
Use a try-except block to handle the ZeroDivisionError exception and display an appropriate error message if the user tries to divide by zero."""

class Division:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        try:
            if self.num2 == 0:
                raise ZeroDivisionError("Error: Cannot divide by zero.")
            result = self.num1 / self.num2
            print(f"The result of division: is: {result}")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")

try:
    # Get user input for the numbers
    num1_input = float(input("Enter the first number: "))
    num2_input = float(input("Enter the second number: "))

    # Create an instance of the Division class with user input
    division_instance = Division(num1_input, num2_input)

  
    division_instance.calculate()

except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print(f"Error: An unexpected error occurred - {e}")



"""10.Write a Python program that simulates a banking system. Implement a class called BankAccount with methods to initialize an account with a starting balance, withdraw funds, and handle a custom exception called NegativeBalanceError when the account balance goes below zero."""

class NegativeBalanceError(Exception):
    pass

# available_balance
balance = 1000 

# Minimum balance requirement
min_balance = 500

# Ask user for the amount to withdraw
withdrawal_amount = int(input("Enter the amount to withdraw: "))

# Check if withdrawal is possible
try:
    if withdrawal_amount > balance:
        raise NegativeBalanceError("Insufficient balance")
    else:
        new_balance = balance - withdrawal_amount
        if new_balance < 0:
            raise NegativeBalanceError("Negative balance after withdrawal.")
        elif new_balance < min_balance:
            print("Withdrawal successful, but your new balance is", new_balance,
                  "which is below the minimum balance of", min_balance, ".")
            print("Please keep your account balance above Rs.500 to avoid unwanted charges.")
        else:
            print("Withdrawal successful. Your new balance is:", new_balance)

except NegativeBalanceError as e:
    print(f"Error: {e}")

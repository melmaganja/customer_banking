"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    class Account:
        def __init__ (self, balance, interest_rate):
            self.balance = balance 
            self.interest_rate = interest_rate 
    
    Account = Account(balance, interest_rate)
    balance = balance = float(input('Enter starting balance: '))
    months = int(input("Enter total months"))

    # Calculate interest earned
     # ADD YOUR CODE HERE
interest_rate = balance * (apr/100 * months/12)
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
savings_account_balance = interest = 0 
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
savings_account = (Account + months)
class savings_account:
    def __init__ (self, balance,interest_rate, months):
        self.balance = balance 
        self.interest_rate = interest_rate
        self. months = months 
    savings_account.set_balance(balance)
    savings_account.set_interest_rate(interest_rate)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
def calculate_interest (self):
    interest_earned = self.balance 
    self.set_interest(interest_earned)
    return interest_earned
    
    # Return the updated balance and interest earned.
 # ADD YOUR CODE HERE

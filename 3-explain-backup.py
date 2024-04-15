

from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
nums = [j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)]

# The code you provided is a list comprehension that generates a list of all the non-prime numbers between 2 and 100.

# - The first line, n = 100, sets the upper bound for the range of numbers to be checked.
# - The second line, sqrt_n = int(sqrt(n)), calculates the square root of the upper bound and converts it to an integer. This value is used to optimize the loop in the list comprehension.
# - The third line, nums = [j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)], is a list comprehension that generates the list of non-prime numbers. The outer loop iterates over all the numbers from 2 to the square root of the upper bound. The inner loop iterates over all the multiples of the outer loop variable, starting from twice the outer loop variable and ending at the upper bound. The multiples of the outer loop variable are non-prime numbers, so they are added to the list.





class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

# Explain this function
# Add additional logic
    def withdraw(self, amount):
        if amount <= 0:
            st.error('Invalid amount')
        elif not self.is_active:
            st.error('Account is not active')
        elif self.is_frozen:
            st.error('Account is frozen')
        else:
            if amount <= self.balance:
                self.balance -= amount
                # Log the withdrawal transaction to a database
                self.log_transaction(amount, 'withdrawal')
                # Send an email or SMS notification to the account holder
                self.send_notification(amount, 'withdrawal')
            else:
                st.error('Insufficient funds')


    def get_balance(self):
        return self.balance
    

# ********** Explaination ****************
# The withdraw method of the BankAccount class checks if the amount to be withdrawn is less than or equal to the current balance of the account. If it is, the amount is subtracted from the balance. If the amount to be withdrawn is greater than the current balance, an error message is printed to the screen.
# This code is important because it ensures that the user cannot withdraw more money than they have in their account. It also provides feedback to the user if they try to withdraw more money than they have.

# Here is a breakdown of the code:

# if amount <= self.balance:: This line checks if the amount to be withdrawn is less than or equal to the current balance of the account.
# self.balance -= amount: If the amount to be withdrawn is less than or equal to the current balance, this line subtracts the amount from the balance.
# else:: If the amount to be withdrawn is greater than the current balance, this block of code is executed.
# st.error('Insufficient funds'): This line prints an error message to the screen.
# Overall, this code is important for ensuring that the user cannot withdraw more money than they have in their account and for providing feedback to the user if they try to do so.
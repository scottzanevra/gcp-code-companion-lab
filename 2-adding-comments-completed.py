# Import the streamlit library
import streamlit as st

# Create a title for the app
st.title('🎈 My Banking App')

# Define a class for the bank account
class BankAccount:
    # Initialize the bank account with a name and balance
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Deposit money into the account
    def deposit(self, amount):
        self.balance += amount

    # Withdraw money from the account
    def withdraw(self, amount):
        # Check if the amount is less than or equal to the balance
        if amount <= self.balance:
            # Subtract the amount from the balance
            self.balance -= amount
        # Otherwise, print an error message
        else:
            st.error('Insufficient funds')

    # Get the balance of the account
    def get_balance(self):
        # Return the balance
        return self.balance


# Get the name of the user
name = st.text_input("Enter your name:")

# Get the initial balance of the account
balance = st.number_input("Enter your initial balance:")

# Create a bank account object
account = BankAccount(name, balance)

# Define a function to deposit money into the account
def deposit_money(account):
    # Get the amount to deposit
    amount = st.number_input("Enter the amount you want to deposit:")
    # Deposit the amount into the account
    account.deposit(amount)

# Define a function to withdraw money from the account
def withdraw_money(account):
    # Get the amount to withdraw
    amount = st.number_input("Enter the amount you want to withdraw:")
    # Withdraw the amount from the account
    account.withdraw(amount)

# Define a function to get the balance of the account
def get_balance(account):
    # Get the balance of the account
    balance = account.get_balance()
    # Return the balance
    return balance

# Withdraw money from the account
withdraw_money(account)

# Get the balance of the account
balance = get_balance(account)

# Print the balance of the account
st.write('The balance of the account is:', balance)

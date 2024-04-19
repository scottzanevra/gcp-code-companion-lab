
# ************************** Code Companion Prompt ***********************************
# Add a comment to each line fo code that explains what it is doing


import streamlit as st

st.title('🎈 My Banking App')

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            st.error('Insufficient funds')

    def get_balance(self):
        return self.balance
    

name = st.text_input("Enter your name:")
balance = st.number_input("Enter your initial balance:")

account = BankAccount(name, balance)

def deposit_money(account):
    amount = st.number_input("Enter the amount you want to deposit:")
    account.deposit(amount)

def withdraw_money(account):
    amount = st.number_input("Enter the amount you want to withdraw:")
    account.withdraw(amount)

def get_balance(account):
    balance = account.get_balance()
    return balance

withdraw_money(account)

balance = get_balance(account)

st.write('The balance of the account is:', balance)
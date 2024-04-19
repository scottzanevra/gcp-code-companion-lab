

# ************************** Code Companion Prompt ***********************************
# Explain this function
from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
nums = [j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)]



# ************************** Code Companion Prompt ***********************************
# Explain this function
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)])) 


# ************************** Code Companion Prompt ***********************************
# Explain this function
lis = [num for num in range(100) if num % 5 == 0 if num % 10 == 0] 



# ************************** Code Companion Prompt ***********************************
# What other methods could be included in this class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
# ************************** Code Companion Prompt ***********************************
# Explain this function
# What additional logic could also be added to the withdraw funtion
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            st.error('Insufficient funds')

    def get_balance(self):
        return self.balance
    



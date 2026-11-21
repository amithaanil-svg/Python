class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount!")

    def display(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)


# Getting input from user
acc_no = int(input("Enter Account Number: "))
name = input("Enter Account Holder Name: ")
acc_type = input("Enter Account Type: ")
balance = float(input("Enter Initial Balance: "))

# Creating object
acc = BankAccount(acc_no, name, acc_type, balance)

acc.display()

# Deposit
d = float(input("\nEnter amount to deposit: "))
acc.deposit(d)
print("Current Balance:", acc.balance)

# Withdrawal
w = float(input("\nEnter amount to withdraw: "))
acc.withdraw(w)
print("Current Balance:", acc.balance)

# Display final details
acc.display()

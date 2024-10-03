import sys

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")
        self.transaction_history.append(f"Checked balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited: ₹{amount}")
            self.transaction_history.append(f"Deposited: ₹{amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"\nWithdrawn: ₹{amount}")
            self.transaction_history.append(f"Withdrawn: ₹{amount}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def view_transaction_history(self):
        print("\nTransaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

    def exit(self):
        print("\nThank you for using the ATM!")
        sys.exit()

def main():
    atm = ATM(1000)  # Starting balance of ₹1000

    while True:
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transaction History")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            try:
                amount = float(input("\nEnter deposit amount: ₹"))
                atm.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == 3:
            try:
                amount = float(input("\nEnter withdrawal amount: ₹"))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == 4:
            atm.view_transaction_history()
        elif choice == 5:
            atm.exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

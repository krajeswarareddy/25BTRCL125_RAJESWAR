class BankAccount:
    """Base class demonstrating encapsulation and core bank operations."""

    bank_name = "BTech National Bank"

    def __init__(self, account_number, holder_name, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = float(initial_balance)  # Encapsulated private attribute
        self.transactions = [f"Account opened with INR {self.__balance:,.2f}"]

    def get_balance(self):
        return self.__balance

    def _update_balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        self.transactions.append(f"Deposited INR {amount:,.2f}")
        print(f"Deposited INR {amount:,.2f}. New Balance: INR {self.__balance:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient balance!")
            return
        self.__balance -= amount
        self.transactions.append(f"Withdrew INR {amount:,.2f}")
        print(f"Withdrew INR {amount:,.2f}. New Balance: INR {self.__balance:,.2f}")

    def display_details(self):
        print("\n--- Account Summary ---")
        print(f"Bank           : {self.bank_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Account Type   : {self.__class__.__name__}")
        print(f"Current Balance: INR {self.__balance:,.2f}")

    def show_transactions(self):
        print("\n--- Transaction History ---")
        for idx, entry in enumerate(self.transactions, start=1):
            print(f"{idx}. {entry}")


class SavingsAccount(BankAccount):
    """Derived class adding interest calculation (Single Inheritance)."""

    def __init__(self, account_number, holder_name, initial_balance=0.0, interest_rate=4.5):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100.0)
        self._update_balance(self.get_balance() + interest)
        self.transactions.append(f"Interest credited ({self.interest_rate}%): INR {interest:,.2f}")
        print(f"Interest of INR {interest:,.2f} credited! New Balance: INR {self.get_balance():,.2f}")


class CurrentAccount(BankAccount):
    """Derived class overriding withdraw() to support overdraft limit (Polymorphism)."""

    def __init__(self, account_number, holder_name, initial_balance=0.0, overdraft_limit=10000.0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.get_balance() + self.overdraft_limit:
            print(f"Exceeds overdraft limit of INR {self.overdraft_limit:,.2f}!")
            return
        self._update_balance(self.get_balance() - amount)
        self.transactions.append(f"Withdrew INR {amount:,.2f} (Overdraft enabled)")
        print(f"Withdrew INR {amount:,.2f}. New Balance: INR {self.get_balance():,.2f}")


def main():
    print("=== Bank Account System (OOP) ===")
    acc_no = input("Enter Account Number (e.g., ACC1001): ").strip() or "ACC1001"
    holder = input("Enter Account Holder Name: ").strip() or "Rajeswar"
    acc_type = input("Select Account Type (1 for Savings, 2 for Current): ").strip()

    try:
        initial = float(input("Enter Initial Deposit (INR): ").strip() or "5000")
    except ValueError:
        initial = 5000.0

    if acc_type == "2":
        account = CurrentAccount(acc_no, holder, initial)
    else:
        account = SavingsAccount(acc_no, holder, initial)

    while True:
        print("\n--- Banking Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. View Account Details")
        print("4. View Transaction History")
        if isinstance(account, SavingsAccount):
            print("5. Calculate & Add Annual Interest")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            try:
                amt = float(input("Enter amount to deposit: "))
                account.deposit(amt)
            except ValueError:
                print("Invalid amount entered.")
        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: "))
                account.withdraw(amt)
            except ValueError:
                print("Invalid amount entered.")
        elif choice == "3":
            account.display_details()
        elif choice == "4":
            account.show_transactions()
        elif choice == "5" and isinstance(account, SavingsAccount):
            account.add_interest()
        elif choice == "0":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
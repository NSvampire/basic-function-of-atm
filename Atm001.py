class ATM:
    def __init__(self):
        self.accounts = {
            "naman": {"pin": "1451", "balance": 10000, "transaction_history": []},
            "steve": {"pin": "2242", "balance": 10000, "transaction_history": []},
            "alex": {"pin": "1733", "balance": 10000, "transaction_history": []}
        }

    def login(self):
        username = input("Enter your username: ").lower()
        pin = input("Enter your PIN: ")

        if username in self.accounts and self.accounts[username]["pin"] == pin:
            return username
        else:
            print("Invalid username or PIN.")
            return None

    def check_balance(self, username):
        balance = self.accounts[username]["balance"]
        print(f"Your current balance is: Rs. {balance}")

    def deposit(self, username):
        amount = float(input("Enter amount to deposit: "))
        self.accounts[username]["balance"] += amount
        self.accounts[username]["transaction_history"].append(f"Deposited Rs. {amount}")

    def withdraw(self, username):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.accounts[username]["balance"]:
            self.accounts[username]["balance"] -= amount
            self.accounts[username]["transaction_history"].append(f"Withdrew Rs. {amount}")
        else:
            print("Insufficient funds.")

    def transfer(self, username):
        recipient = input("Enter recipient's username: ").lower()
        if recipient in self.accounts:
            amount = float(input("Enter amount to transfer: "))
            if amount <= self.accounts[username]["balance"]:
                self.accounts[username]["balance"] -= amount
                self.accounts[recipient]["balance"] += amount
                self.accounts[username]["transaction_history"].append(f"Transferred Rs. {amount} to {recipient}")
                self.accounts[recipient]["transaction_history"].append(f"Received Rs. {amount} from {username}")
            else:
                print("Insufficient funds.")
        else:
            print("Recipient not found.")

    def transaction_history(self, username):
        print("Transaction History:")
        for transaction in self.accounts[username]["transaction_history"]:
            print(transaction)

    def menu(self, username):
        while True:
            print("\nMenu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Transaction History")
            print("6. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance(username)
            elif choice == "2":
                self.deposit(username)
            elif choice == "3":
                self.withdraw(username)
            elif choice == "4":
                self.transfer(username)
            elif choice == "5":
                self.transaction_history(username)
            elif choice == "6":
                print("Logged out.")
                break
            else:
                print("Invalid choice.")


atm = ATM()

print("""
   ###########################################################
   #######                                            ########
   #######                WELCOME                     ########
   #######                                            ########
   ###########################################################
""")

while True:
    print("\nWelcome to the ATM")
    username = atm.login()
    if username:
        atm.menu(username)
    else:
        continue

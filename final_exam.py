import random
class Bank:
    def __init__(self):
        self.users = {}
        self.admin_password = "admin123"
        self.loan_feature = True
        self.is_bankrupt = False
        self.total_balance = 0
        self.total_loan_amount = 0

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(1000,9999)
        user = {
            "name": name,
            "email": email,
            "address": address,
            "account_type": account_type,
            "account_number": account_number,
            "balance": 0,
            "loan_taken": 0,
            "transaction_history": []
        }
        self.users[account_number] = user
        return account_number

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.users[account_number]["balance"] += amount
            self.total_balance += amount
            self.users[account_number]["transaction_history"].append(f"Deposited: {amount}")
            print("Deposit successful")

    def withdraw(self, account_number, amount):
        if self.is_bankrupt == True:
            print(" The bank is bankrupt")
        else:
            if amount <= 0:
                print("Invalid amount")
            elif amount > self.users[account_number]["balance"]:
                print("Withdrawal amount exceeded” 										")
            else:
                self.users[account_number]["balance"] -= amount
                self.total_balance -= amount
                self.users[account_number]["transaction_history"].append(f"Withdraw: {amount}")
                print("Withdraw successful")

    def check_balance(self, account_number):
        return self.users[account_number]["balance"]

    def check_transaction_history(self, account_number):
        return self.users[account_number]["transaction_history"]

    def take_loan(self, account_number, loan_amount):
        if self.users[account_number]["loan_taken"] < 2 and self.loan_feature:
            self.users[account_number]["balance"] += loan_amount
            self.users[account_number]["loan_taken"] += 1
            self.total_loan_amount += loan_amount
            self.users[account_number]["transaction_history"].append(f"Loan Taken: {loan_amount}")
            return "Loan taken successfully"
        else:
            return "Cannot take more loans"

    def transfer(self, from_account_number, to_account_number, amount):
        if self.is_bankrupt == True:
            return "The bank is bankrupt"
        else:
            if to_account_number not in self.users:
                return "Account does not exist"
            elif self.users[from_account_number]["balance"] < amount:
                return "Insufficient balance"
            else:
                self.users[from_account_number]["balance"] -= amount
                self.users[to_account_number]["balance"] += amount
                self.users[from_account_number]["transaction_history"].append(f"Transferred: {amount} to {to_account_number}")
                self.users[to_account_number]["transaction_history"].append(f"Received: {amount} from {from_account_number}")
                return "Transfer successful"

    def admin_login(self, password):
        return password == self.admin_password

    def delete_account(self, account_number):
        del self.users[account_number]

    def list_accounts(self):
        return self.users

    def ttotal_balance(self):
        return self.total_balance

    def ttotal_loan_amount(self):
        return self.total_loan_amount

    def check_loan_feature(self):
        self.loan_feature = not self.loan_feature
    def check_bankrupt(self):
        self.is_bankrupt = not self.is_bankrupt

bank = Bank()
def user_login():
        print("\tUSER LOGIN")
        account_number = int(input("Enter your account number: "))
        if account_number in bank.list_accounts():
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7. Logout")
                option = int(input("Enter your option: "))

                if option == 1:
                    amount = float(input("Enter amount to deposit: "))
                    bank.deposit(account_number, amount)

                elif option == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    result = bank.withdraw(account_number, amount)
                    
                elif option == 3:
                    print("Available Balance:", bank.check_balance(account_number))

                elif option == 4:
                    print("Transaction History:", bank.check_transaction_history(account_number))
                
                elif option == 5:
                    loan_amount = float(input("Enter loan amount: "))
                    print(bank.take_loan(account_number, loan_amount))
                
                elif option == 6:
                    to_account_number = int(input("Enter receiver account number: "))
                    amount = float(input("Enter amount to transfer: "))
                    result = bank.transfer(account_number, to_account_number, amount)
                    print(result)
                
                elif option == 7:
                    break
                    
                else:
                    print("Invalid option. Please try again.")

        else:
            print("Invalid account number. Please try again.")
def admin_login():
        password = input("Enter admin password: ")
        if bank.admin_login(password):
            while True:
                print("\tADMIN LOGIN")
                print("1. Create account")
                print("2. Delete account")
                print("3. View all accounts")
                print("4. Check total balance")
                print("5. Check total loan amount")
                print("6. Change Loan Feature")
                print("7. Change bankrupt")
                print("8. Logout")
                option = int(input("Enter your option: "))

                if option == 1:
                    name = input("Enter user's name: ")
                    email = input("Enter user's email: ")
                    address = input("Enter user's address: ")
                    account_type = input("Enter account type (Savings/Current): ")
                    account_number = bank.create_account(name, email, address, account_type)
                    print(f"Account created successfully. Your account number is: {account_number}")
                elif option == 2:
                    account_number = int(input("Enter account number to delete: "))
                    bank.delete_account(account_number)
                    print("Account deleted successfully.")
                elif option == 3:
                    print("All accounts:", bank.list_accounts())
                elif option == 4:
                    print("Total balance:", bank.ttotal_balance())
                elif option == 5:
                    print("Total loan amount:", bank.ttotal_loan_amount())
                elif option == 6:
                    bank.check_loan_feature()
                    if bank.loan_feature:
                        status = "enable"
                    else:
                        status = "disable"
                    print(f"Loan feature {status} successfully.")
                elif option == 7:
                    bank.check_bankrupt()

                elif option == 8:
                    break
    
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid admin password. Please try again.")

run = True
while run:
        print("\tWELCOME TO BANK MANAGEMENT SYSTEM\n")
        print("1. User login")
        print("2. Admin login")
        print("3. Create an account")
        print("4. Exit")
        option = int(input("Enter your option: "))

        if option == 1:
            user_login()
        elif option == 2:
            admin_login()
        elif option == 3:
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type (Savings/Current): ")
            account_number = bank.create_account(name, email, address, account_type)
            print(f"Account created successfully. Your account number is: {account_number}")
        elif option == 4:
            run = False
            break
        else:
            print("Invalid option. Please try again.")
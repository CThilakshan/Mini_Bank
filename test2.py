import json
import os
import datetime
import getpass


date_time = datetime.datetime.now()
accounts = {}
account_number = 550000

Admin_username = "admin"
Admin_password = "admin123"
FILE_NAME = "account.txt"

def save_accounts():
    with open(FILE_NAME, "w") as f:
        json.dump(accounts, f)

def load_accounts():
    global accounts
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            accounts.update(json.load(f))

def get_next_account_number():
    if accounts:
        return max(map(int, accounts.keys())) + 1
    else:
        return 550001

def login():
    load_accounts()
    while True:
        print("1. Admin Login".center(200))
        print("2. Customer Login".center(200))
        print("3. Exit".center(200))
        choice = input("Choose login type:").strip()

        if choice == '1':
            access="admin"
            username = input("\nEnter Admin username: ").strip()
            password = getpass.getpass("Enter Admin password: ").strip()
            if username == Admin_username and password == Admin_password:
                print("\n=== Admin login successful ===")
                admin_menu(access)
                break
            else:
                print("Invalid admin credentials.")
        elif choice == '2':
            try:
                access="customer"
                acc_num = input("\nEnter your account number: ").strip()
                password = getpass.getpass("Enter your password:").strip()
                if acc_num in accounts and accounts[acc_num]["password"] == password:
                    print("=== Customer login successful ===")
                    customer_menu(acc_num,access)
                    break
                else:
                    print("Invalid account number or password.")
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            print("Thank you")
            break
        else:
            print("Invalid choice.")

def admin_menu(access):
    while True:
        print("\nAdmin Menu")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Show Balance")
        print("6. Transaction History")
        print("7. Logout")
        choice = input("Choose an option:(1-7) ").strip()

        if choice == '1':
            create_customer()
        elif choice == '2':
            create_account()
        elif choice == '3':
            deposit_money(None,access)
        elif choice == '4':
            withdraw_money(None,access)
        elif choice == '5':
            show_balance(None)
        elif choice == '6':
            transaction_history(None)
        elif choice == '7':
            print("Logging out...")
            login()
        else:
            print("Invalid choice.")

def customer_menu(acc_num,access):
    while True:
        print("\nCustomer Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Account to Account Transfer")
        print("4. Show Balance")
        print("5. Transaction History")
        print("6. Logout\n")
        choice = input("Choose an option:(1-6) ").strip()

        if choice == '1':
            deposit_money(acc_num,access)
        elif choice == '2':
            withdraw_money(acc_num,access)
        elif choice == '3':
            account_to_account_transfer(acc_num,access)
        elif choice == '4':
            show_balance(acc_num)
        elif choice == '5':
            transaction_history(acc_num)
        elif choice == '6':
            print("Logging out...")
            login()
        else:
            print("Invalid choice.")

def create_customer():
    global account_number
    name = input("Enter customer name: ").strip()
    password = input("Enter customer password: ").strip()
    initial_balance = int(input("Enter initial deposit amount: "))

    if initial_balance < 0:
        print("Initial deposit cannot be negative.")
        return

    acc_num = str(get_next_account_number())
    accounts[acc_num] = {
        "name": name,
        "password": password,
        "balance": initial_balance,
        "transactions": []
    }
    save_accounts()
    print(f"Customer created successfully. Account number: {acc_num}.")
    print(f"Account password is {password}.")

def create_account():
    name = input("Enter your name: ").strip()
    password = input("Enter your password: ").strip()
    initial_balance = int(input("Enter initial deposit amount: "))

    if initial_balance < 0:
        print("Initial deposit cannot be negative.")
        return

    acc_num = str(get_next_account_number())
    accounts[acc_num] = {
        "name": name,
        "password": password,
        "balance": initial_balance,
        "datetime":date_time.strftime('%x %X'),
        "transactions": []
    }
    save_accounts()
    print(f"Account created successfully. Your account number is {acc_num}.")
    print(f"Account password is {password}.")
    print(f"Initial balance is {initial_balance}.")

def deposit_money(acc_num=None,access=None):
    deposit_acnum = input("Enter your account number: ").strip()
    if acc_num == deposit_acnum or access == "admin":
        acc_num=deposit_acnum
        try:
            amount = int(input("Enter amount to deposit: "))
            if acc_num in accounts and amount > 0:
                accounts[acc_num]["balance"] += amount
                accounts[acc_num]["transactions"].append(f"Date and time: {date_time.strftime('%x %X')} - Deposited: {amount}, Balance: {accounts[acc_num]['balance']},Access:{access}")
                save_accounts()
                print(f"Deposited {amount} to account {acc_num}. New balance: {accounts[acc_num]['balance']}")
        except ValueError:
                print("Invalid Amount.")
    else:
        print("Invaild Account Number")    

def withdraw_money(acc_num=None,access=None):
    withdraw_acnum = input("Enter your account number: ").strip()
    if acc_num== withdraw_acnum or access =="admin":
        try:
            acc_num=withdraw_acnum
            amount = int(input("Enter amount to withdraw: "))
            if acc_num in accounts and 0 < amount <= accounts[acc_num]["balance"]:
                accounts[acc_num]["balance"] -= amount
                accounts[acc_num]["transactions"].append(f"{date_time.strftime('%x %X')} - Withdrawn: {amount}, Balance: {accounts[acc_num]['balance']},Access:{access}")
                save_accounts()
                print(f"Withdrew {amount} from account {acc_num}. New balance: {accounts[acc_num]['balance']}")
            else:
                print("Invalid account number or amount.")
        except ValueError:
            print("Invalid input.")

def account_to_account_transfer(acc_num=None,access=None):
    from_acc_num = input("Enter your account number: ").strip()
    if acc_num==from_acc_num :
        try:
            to_acc_num = input("Enter the account number to transfer to: ").strip()
            amount = int(input("Enter amount to transfer: "))

            if from_acc_num in accounts and to_acc_num in accounts and 0 < amount <= accounts[from_acc_num]["balance"]:
                accounts[from_acc_num]["balance"] -= amount
                accounts[to_acc_num]["balance"] += amount
                accounts[from_acc_num]["transactions"].append(f"{date_time.strftime('%x %X')} - Transferred Rs.{amount} to account {to_acc_num}")
                accounts[to_acc_num]["transactions"].append(f"{date_time.strftime('%x %X')} - Received Rs.{amount} from account {from_acc_num}")
                save_accounts()
                print(f"Transferred {amount} from account {from_acc_num} to account {to_acc_num}.")
            else:
                print("Invalid Amount.")
        except ValueError:
            print("Invalid input.")
    else:
        print("Invalid account numbers.")
        

def show_balance(acc_num=None):
    show_num = input("Enter your account number: ").strip()
    if acc_num==show_num:
        if acc_num in accounts:
            print(f"Account {acc_num} balance: {accounts[acc_num]['balance']}")
        else:
            print("Invalid account number.")

def transaction_history(acc_num=None):
    acc_num = acc_num or input("Enter your account number: ").strip()
    if acc_num in accounts:
        print(f"Transaction history for account {acc_num}:")
        for transaction in accounts[acc_num]["transactions"]:
            print(transaction)
    else:
        print("Invalid account number.")

# Application calling
login()
#testing two

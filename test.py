import datetime

accounts = {}
account_number = 550000

Admin_username = "admin"
Admin_password = "admin123"

def create_customer():
    global account_number
    name = input("Enter customer name: ").strip()
    password = input("Enter customer password: ").strip()
    initial_balance = int(input("Enter initial deposit amount: "))

    if initial_balance < 0:
        print("Initial deposit cannot be negative.")
        return

    account_number += 1
    accounts[account_number] = {
        "name": name,
        "password": password,
        "balance": initial_balance,
        "transactions": []
    }
    print(f"Customer created successfully. Account number: {account_number}.")
    print(f"Account password is {password}.")

def create_account():
    global account_number
    name = input("Enter your name: ").strip()
    password = input("Enter your password: ").strip()
    initial_balance = int(input("Enter initial deposit amount: "))

    if initial_balance < 0:
        print("Initial deposit cannot be negative.")
        return

    account_number += 1
    accounts[account_number] = {
        "name": name,
        "password": password,
        "balance": initial_balance,
        "transactions": []
    }
    print(f"Account created successfully. Your account number is {account_number}.")
    print(f"Account password is {password}.")
    print(f"Initial balance is {initial_balance}.")

def deposit_money(acc_num):
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            accounts[acc_num]["balance"] += amount
            timestamp = datetime.datetime.now()
            accounts[acc_num]["transactions"].append(f"{timestamp} - Deposited: {amount}, Balance: {accounts[acc_num]['balance']}")
            print(f"Deposited {amount}. New balance: {accounts[acc_num]['balance']}")
        else:
            print("Amount must be positive.")
    except ValueError:
        print("Invalid input.")

def withdraw_money(acc_num):
    try:
        amount = int(input("Enter amount to withdraw: "))
        if 0 < amount <= accounts[acc_num]["balance"]:
            accounts[acc_num]["balance"] -= amount
            timestamp = datetime.datetime.now()
            accounts[acc_num]["transactions"].append(f"{timestamp} - Withdrawn: {amount}, Balance: {accounts[acc_num]['balance']}")
            print(f"Withdrew {amount}. New balance: {accounts[acc_num]['balance']}")
        else:
            print("Invalid amount.")
    except ValueError:
        print("Invalid input.")

def account_to_account_transfer(acc_num):
    try:
        to_acc_num = int(input("Enter account number to transfer to: "))
        amount = int(input("Enter amount to transfer: "))

        if to_acc_num in accounts and 0 < amount <= accounts[acc_num]["balance"]:
            accounts[acc_num]["balance"] -= amount
            accounts[to_acc_num]["balance"] += amount
            timestamp = datetime.datetime.now()
            accounts[acc_num]["transactions"].append(f"{timestamp} - Transferred {amount} to {to_acc_num}, Balance: {accounts[acc_num]['balance']}")
            accounts[to_acc_num]["transactions"].append(f"{timestamp} - Received {amount} from {acc_num}, Balance: {accounts[to_acc_num]['balance']}")
            print(f"Transferred {amount} to account {to_acc_num}.")
        else:
            print("Invalid account or insufficient funds.")
    except ValueError:
        print("Invalid input.")

def show_balance(acc_num):
    print(f"Account {acc_num} balance: {accounts[acc_num]['balance']}")

def transaction_history(acc_num):
    print(f"Transaction history for account {acc_num}:")
    for transaction in accounts[acc_num]["transactions"]:
        print(transaction)

def customer_menu(acc_num):
    while True:
        print("\nCustomer Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Account to Account Transfer")
        print("4. Show Balance")
        print("5. Transaction History")
        print("6. Logout")

        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            deposit_money(acc_num)
        elif choice == '2':
            withdraw_money(acc_num)
        elif choice == '3':
            account_to_account_transfer(acc_num)
        elif choice == '4':
            show_balance(acc_num)
        elif choice == '5':
            transaction_history(acc_num)
        elif choice == '6':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Show All Accounts")
        print("4. Logout")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            create_customer()
        elif choice == '2':
            create_account()
        elif choice == '3':
            for acc, data in accounts.items():
                print(f"Account: {acc}, Name: {data['name']}, Balance: {data['balance']}")
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def login():
    while True:
        print("\n" + "-"*20 + " LOGIN MENU " + "-"*20)
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Choose login type: ").strip()

        if choice == '1':
            username = input("Enter Admin username: ").strip()
            password = input("Enter Admin password: ").strip()
            if username == Admin_username and password == Admin_password:
                print("Admin login successful.")
                admin_menu()
            else:
                print("Invalid admin credentials.")
        elif choice == '2':
            try:
                acc_num = int(input("Enter your account number: "))
                password = input("Enter your password: ").strip()
                if acc_num in accounts and accounts[acc_num]["password"] == password:
                    print("Customer login successful.")
                    customer_menu(acc_num)
                else:
                    print("Invalid account number or password.")
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Start the program
login()

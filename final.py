import datetime
x = datetime.datetime.now()
accounts={}
account_number =550000

Admin_username="admin"
Admin_password="admin123"

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

    admin_menu()
    
def login():
    while True:
        global account_number
        print("1. Admin Login".center(200))
        print("2. Customer Login".center(200))
        print("3. Exit".center(200))
        choice = input("Choose login type:").strip()

        if choice == '1':
            username = input("\nEnter Admin username: ").strip()
            password = input("Enter Admin password: ").strip()
            if username == Admin_username and password == Admin_password:
                print("\n===================================================================             Admin login successful            =======================================================================")
                admin_menu()
            else:
                print("=====================================================================           Invalid admin credentials           =======================================================================")
        elif choice == '2':
            try:
                acc_num = int(input("\nEnter your account number: "))
                password = input("Enter your password:").strip()
                if acc_num in accounts and accounts[acc_num]["password"] == password:
                    print("\n===============================================================           Customer login successful           =======================================================================")
                    return acc_num,customer_menu()
                else:
                    print("\n===============================================================      Invalid account number or password       =======================================================================")
            except ValueError:
                print("\n===================================================================                 Invalid input                 =======================================================================")
        elif choice =='3':
            break
        else:
            print("\n=======================================================================                Invalid choice                 =======================================================================")

def admin_menu():
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
            deposit_money(acc_num)
        elif choice == '4':
            withdraw_money(acc_num)
        elif choice == '5':
            show_balance(acc_num)
        elif choice == '6':
            transaction_history(acc_num)
        elif choice == '7':
            print("Logging out...")
            login()
        else:
            print("Invalid choice.")

def customer_menu() :
    while True:
        print("\nCustomer Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3.Account to Account Transfer")
        print("4. Show Balance")
        print("5. Transaction History")
        print("6. Logout\n")
        choice = input("Choose an option:(1-6) ").strip()

        if choice == '1':
            deposit_money()
        elif choice == '2':
            withdraw_money()
        elif choice == '3': 
            account_to_account_transfer()
        elif choice == '4':         
            show_balance()
        elif choice == '5':
            transaction_history()
        elif choice == '6':
            print("Logging out...")
            break
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

    account_number += 1
    accounts[account_number] = {
        "name": name,
        "password": password,
        "balance": initial_balance,
        "transactions": []
    }
    print(f"Customer created successfully. Account number: {account_number}.")
    print(f"Account password is {password}.")

    admin_menu()

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
        acc_num = int(input("Enter your account number: "))
        amount = int(input("Enter amount to deposit: "))

        if acc_num in accounts and amount > 0:
            accounts[acc_num]["balance"] += amount
            accounts[acc_num]["transactions"].append(f"Dateandtime:{x},Deposited: {amount},balance: {accounts[acc_num]['balance']}")
            print(accounts)
            print(f"Deposited {amount} to account {acc_num}. New balance: {accounts[acc_num]['balance']}")
        else:
            print("Invalid account number or amount.")
    except ValueError:
        print("Invalid input.")

def withdraw_money(acc_num):
    try:
        acc_num = int(input("Enter your account number: "))
        amount = int(input("Enter amount to withdraw: "))

        if acc_num in accounts and 0 < amount <= accounts[acc_num]["balance"]:
            accounts[acc_num]["balance"] -= amount
            accounts[acc_num]["transactions"].append(f"Dateandtime:{x},Withdrawn: {amount},balance: {accounts[acc_num]['balance']}")
            print(accounts)
            print(f"Withdrew {amount} from account {acc_num}. New balance: {accounts[acc_num]['balance']}")
        else:
            print("Invalid account number or amount.")
    except ValueError:
        print("Invalid input.")

def account_to_account_transfer(acc_num):
    try:
        from_acc_num = int(input("Enter your account number: "))
        to_acc_num = int(input("Enter the account number to transfer to: "))
        amount = int(input("Enter amount to transfer: "))

        if from_acc_num in accounts and to_acc_num in accounts and 0 < amount <= accounts[from_acc_num]["balance"]:
            accounts[from_acc_num]["balance"] -= amount
            accounts[to_acc_num]["balance"] += amount
            accounts[from_acc_num]["transactions"].append(f"Dateandtime:{x},Transferred Rs.{amount} to account {to_acc_num},balance: {accounts[from_acc_num]['balance']}")
            accounts[to_acc_num]["transactions"].append(f"Dateandtime:{x},Received Rs.{amount} from account {from_acc_num},balance: {accounts[to_acc_num]['balance']}")
            print(f"Transferred {amount} from account {from_acc_num} to account {to_acc_num}.")
        else:
            print("Invalid account numbers or amount.")
    except ValueError:
        print("Invalid input.")

def show_balance(acc_num):
    try:
        acc_num = int(input("Enter your account number: "))

        if acc_num in accounts:
            print(f"Account {acc_num} balance: {accounts[acc_num]['balance']}")
        else:
            print("Invalid account number.")
    except ValueError:
        print("Invalid input.")

def transaction_history(acc_num):
    try:
        acc_num = int(input("Enter your account number: "))

        if acc_num in accounts:
            print(f"Transaction history for account {acc_num}:")
            for transaction in accounts[acc_num]["transactions"]:
                print(transaction)
        else:
            print("Invalid account number.")
    except ValueError:
        print("Invalid input.")

login()





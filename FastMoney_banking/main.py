# FastMoney Banking
# Need to build out frontend and validation for users and database
import datetime 
import os
import platform

# global variables
transactions = []
dashes = '************************************************'

# Function to check if user inputs an float int for deposit/withdrawal
def clear_screen():
    # Check the operating system and clear the screen accordingly
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def check_if_number(n) :
    try :
        float(n)
        return True
    except ValueError :
        return False

# get User Account Information
def get_userinfo() :
    # Account Holder Name
    sanitized_name = []
    name = input('What is your name? ').lower()
    name_list = name.split()
    for element in name_list :
        string = element[0].capitalize() + element[1:]
        sanitized_name.append(string)
    sanitized_name_str = ' '.join(sanitized_name)

    # Sanitized Account Number
    sanitize_acct_num = []
    acct_num = input('Enter your 10-digit account number(ex: 1010101010):  ')
    print(f'\n{dashes}')
    if len(acct_num) < 10 :
        print('Account number is not 10 digits long.')
        acct_num = input('Enter your 10-digit account number(ex: 1010101010):  ')
    for i, num in enumerate(acct_num) :
        if i <= 5 :
            sanitize_acct_num.append('*')
        else :
            sanitize_acct_num.append(str(num))      
    sanitize_acct_num_str = ''.join(sanitize_acct_num)

    return [sanitized_name_str, sanitize_acct_num_str]

# Function to append a transaction
def add_transaction(transaction):
    global transactions
    transactions.append(transaction)
    print(f"Transaction processed: {transaction}\n")

# Function to print the list of transactions
def print_transactions():
    global transactions
    global balance
    print(f'\n{dashes}')
    if transactions:
        print("Transactions:")
        for index, transaction in enumerate(transactions, start=1):
            print(f"{index}. {transaction}")        
    else:
        print("No transactions available.")

# Function to print the current balance for request 1:   
def show_balance(balance) :
    curr_balance = f'$ {balance:,.2f}\n'
    print('\nYour current balance: ', curr_balance)

# Function to deposit amount given, update balance and add to transactions:
def deposit() : 
    print('\nMake a Deposit: \n')
    amount = input('Enter the amount to be deposited. $ ')
    valid_amount = check_if_number(amount)
    if valid_amount :
        amount = float(amount)
        if amount > 0 :
            deposit = f'Deposit: $ {amount:,.2f}'
            add_transaction(deposit)
            return amount
    else :
        print('Not a valid deposit.')
        return 0

# Function to withdraw amount given, update balance and add to transactions:   
def withdraw(balance) :
    print('\nMake a Withdrawal: \n')
    amount = input('Enter amount to be withdrawn: $ ')
    valid_amt = check_if_number(amount)
    if valid_amt :
        amount = float(amount)
        if amount > balance :
            print(f'\nInsufficient funds. Your balance is ${balance:,.2f}.\n')
            print(f'{dashes}\n')
            return 0
        elif amount < 0 :
            print('Amount must be greater than zero.\n')
            return 0
        else :
            withdrawal = f'Withdrawal: $ {amount:,.2f}'
            add_transaction(withdrawal)
            return amount   
            
# Main bank appt while interacting with user:  
def main() :
    balance = 0
    global transactions
    is_running = True
    print(f'\n{dashes}\n')
    print(f'Welcome to FastMoney Banking!\n')
    print(f'{dashes}\n')
    name, acct_num = get_userinfo()
    clear_screen()
    while is_running :
        now = datetime.datetime.now()
        date_time_str = now.strftime("%B %d, %Y %I:%M %p").lower()
        date_time_str = date_time_str.lstrip('0').replace(' 0', ' ')
        print(f'{dashes}')
        print(f'FastMoney Banking -- {(date_time_str).capitalize()}\n')
        print(f'For: {name}')
        print(f'Account Number: {acct_num}\n')
        print(f'{dashes}')
        print(f'How can we help?')
        print('1. Show Balance')
        print('2. Deposit Funds')
        print('3. Withdraw Funds')
        print('4. Get Your Transactions')
        print('5. Exit Bank Program')
        choice = input("Enter your bank choice (1-5):  ")
        clear_screen()
        if choice == '1' :
            show_balance(balance)
        elif choice == '2' :
            balance += deposit()
            show_balance(balance)
        elif choice == '3' :
            balance -= withdraw(balance)
            show_balance(balance)
        elif choice == '4' :
            print_transactions()
            show_balance(balance)
            is_running = True          
        elif choice == '5' :
            is_running = False
        else :
            print('\nThat is not a valid choice.')
            print(f'{dashes}\n')

    # Exit banking with option to re-start      
    clear_screen()
    print(f'\n{dashes}')
    print('\nThank you for using FastMoney Banking!\n')
    if __name__=='__main__' :
        main()

# Start Banking
if __name__=='__main__' :
    main()


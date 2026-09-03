# 3. Develop a package banking containing:
# a) account.py – account creation and balance
# b) transaction.py – deposit and withdrawal
# c) loan.py – loan calculation
# Create a main program to use the package.


from banking.account import create_account, check_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_interest, calculate_total_amount


name = input("Enter account holder name: ")

account_number = input("Enter account number: ")

balance = float(input("Enter initial balance: "))


account = create_account(
    name,
    account_number,
    balance
)


print("\n----- ACCOUNT DETAILS -----")

print("Name:", account["name"])

print("Account Number:", account["account_number"])

print("Balance:", check_balance(account))


deposit_amount = float(input("\nEnter deposit amount: "))

deposit(account, deposit_amount)

print("Balance after deposit:", check_balance(account))


withdraw_amount = float(input("Enter withdrawal amount: "))

withdraw(account, withdraw_amount)

print("Balance after withdrawal:", check_balance(account))


principal = float(input("\nEnter loan amount: "))

rate = float(input("Enter interest rate: "))

years = int(input("Enter loan period in years: "))


interest = calculate_interest(
    principal,
    rate,
    years
)

total_amount = calculate_total_amount(
    principal,
    rate,
    years
)


print("\n----- LOAN DETAILS -----")

print("Loan Amount:", principal)

print("Interest:", interest)

print("Total Amount:", total_amount)

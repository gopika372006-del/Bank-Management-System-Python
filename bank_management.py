
print("================================")
print("     BANK MANAGEMENT SYSTEM")
print("================================")

print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Check Balance")
print("5. View Account")
print("6. Exit")

choice = input("Enter your choice: ")

print("Your choice is:", choice)


import json
import os

FILE_NAME = "bank_data.json"


# Load account details from file
def load_accounts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read account data.")
            return {}
    return {}


# Save account details to file
def save_accounts():
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


accounts = load_accounts()


# Generate a new account number
def generate_account_number():
    numbers = [int(number) for number in accounts.keys()]
    return str(max(numbers, default=1000) + 1)


# Create a new bank account
def create_account():
    print("\n--- CREATE BANK ACCOUNT ---")

    name = input("Enter customer name: ").strip()

    if not name or not name.replace(" ", "").isalpha():
        print("Invalid name. Use letters and spaces only.")
        return

    phone = input("Enter phone number: ").strip()

    if not phone.isdigit() or len(phone) != 10:
        print("Enter a valid 10-digit phone number.")
        return

    for account in accounts.values():
        if account["phone"] == phone:
            print("An account with this phone number already exists.")
            return

    try:
        opening_balance = float(input("Enter opening balance: "))

        if not 0 <= opening_balance <= 10000000:
            print("Enter a balance between 0 and 10000000.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "balance": round(opening_balance, 2)
    }

    save_accounts()

    print("\nAccount created successfully!")
    print("Account Number:", account_number)
    print("Customer Name:", name)
    print("Opening Balance: Rs.", f"{opening_balance:.2f}")


# View one account
def view_account():
    print("\n--- VIEW ACCOUNT DETAILS ---")

    account_number = input("Enter account number: ").strip()

    if account_number in accounts:
        account = accounts[account_number]

        print("\nAccount Number:", account_number)
        print("Customer Name:", account["name"])
        print("Phone Number:", account["phone"])
        print("Available Balance: Rs.", f'{account["balance"]:.2f}')
    else:
        print("Account not found.")


# Deposit money
def deposit_money():
    print("\n--- DEPOSIT MONEY ---")

    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount: "))

        if not 0 < amount <= 10000000:
            print("Enter an amount greater than zero.")
            return

        account = accounts[account_number]
        account["balance"] = round(account["balance"] + amount, 2)

        save_accounts()

        print("Deposit successful!")
        print("Current Balance: Rs.", f'{account["balance"]:.2f}')

    except ValueError:
        print("Please enter a valid amount.")


# Withdraw money
def withdraw_money():
    print("\n--- WITHDRAW MONEY ---")

    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))

        if not 0 < amount <= 10000000:
            print("Enter an amount greater than zero.")
            return

        account = accounts[account_number]

        if amount > account["balance"]:
            print("Insufficient balance!")
            return

        account["balance"] = round(account["balance"] - amount, 2)

        save_accounts()

        print("Withdrawal successful!")
        print("Remaining Balance: Rs.", f'{account["balance"]:.2f}')

    except ValueError:
        print("Please enter a valid amount.")


# Check balance
def check_balance():
    print("\n--- CHECK BALANCE ---")

    account_number = input("Enter account number: ").strip()

    if account_number in accounts:
        balance = accounts[account_number]["balance"]
        print("Available Balance: Rs.", f"{balance:.2f}")
    else:
        print("Account not found.")


# Search account by number or customer name
def search_account():
    print("\n--- SEARCH ACCOUNT ---")
    keyword = input("Enter account number or customer name: ").strip().lower()

    found = False

    for number, account in accounts.items():
        if (keyword == number or
                keyword in account["name"].lower()):

            print("\nAccount Number:", number)
            print("Customer Name:", account["name"])
            print("Phone Number:", account["phone"])
            print("Balance: Rs.", f'{account["balance"]:.2f}')
            found = True

    if not found:
        print("No matching account found.")


# Display all accounts
def view_all_accounts():
    print("\n--- ALL BANK ACCOUNTS ---")

    if not accounts:
        print("No accounts available.")
        return

    for number, account in accounts.items():
        print("-" * 30)
        print("Account Number:", number)
        print("Customer Name:", account["name"])
        print("Phone Number:", account["phone"])
        print("Balance: Rs.", f'{account["balance"]:.2f}')


# Main menu
def main():
    while True:
        print("\n" + "=" * 36)
        print("       BANK MANAGEMENT SYSTEM")
        print("=" * 36)
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Search Account")
        print("7. View All Accounts")
        print("8. Exit")
        print("=" * 36)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            view_account()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            withdraw_money()
        elif choice == "5":
            check_balance()
        elif choice == "6":
            search_account()
        elif choice == "7":
            view_all_accounts()
        elif choice == "8":
            print("Thank you for using Bank Management System!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1 to 8.")


if __name__ == "__main__":
    main()

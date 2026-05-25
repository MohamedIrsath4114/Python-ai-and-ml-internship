
# Simple ATM Machine Program

balance = 5000
pin = "1234"

# Function to check balance
def check_balance():
    print(f"Your current balance is: ₹{balance}\n")


# Function to deposit money
def deposit_money():
    global balance

    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        print(f"₹{amount} deposited successfully!")
        print(f"Updated Balance: ₹{balance}\n")
    else:
        print("Invalid deposit amount!\n")


# Function to withdraw money
def withdraw_money():
    global balance

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid withdrawal amount!\n")

    elif amount > balance:
        print("Insufficient balance!\n")

    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully!")
        print(f"Remaining Balance: ₹{balance}\n")


# Function to change PIN
def change_pin():
    global pin

    old_pin = input("Enter current PIN: ")

    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        pin = new_pin
        print("PIN changed successfully!\n")
    else:
        print("Incorrect current PIN!\n")


# Main ATM Menu using while loop
while True:
    print("===== ATM MACHINE =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        check_balance()

    elif choice == '2':
        deposit_money()

    elif choice == '3':
        withdraw_money()

    elif choice == '4':
        change_pin()

    elif choice == '5':
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please try again.\n")

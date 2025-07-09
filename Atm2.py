# Cards
cards = {
    "A1": [1111, 50000.00],
    "A2": [2222, 60000.00],
    "A3": [3333, 70000.00],
    "A4": [4444, 80000.00]
}

def show_menu():
    print("Press\n1 for Balance Enquiry\n2 for Withdraw\n3 for Deposit\n4 for Change Pin\n5 for Exit")

def balance_enquiry(card_number):
    print(f"Card Number: {card_number}")
    print(f"Available Balance: Rs.{cards[card_number][1]}")

def withdraw(card_number):
    amount = float(input("Enter the Amount: "))
    if 0 < amount <= cards[card_number][1]:
        cards[card_number][1] -= amount
        print(f"{card_number} Debited for Rs.{amount} and Avl Balance Rs.{cards[card_number][1]}")
    else:
        print("Insufficient Funds")

def deposit(card_number):
    amount = float(input("Enter the Amount: "))
    if amount > 0:
        cards[card_number][1] += amount
        print(f"{card_number} Credited for Rs.{amount} and Avl Balance Rs.{cards[card_number][1]}")
    else:
        print("Invalid Amount")

def change_pin(card_number):
    current_pin = int(input("Enter Your Current PIN: "))
    if current_pin == cards[card_number][0]:
        new_pin = int(input("Enter New PIN: "))
        cards[card_number][0] = new_pin
        print("PIN Updated Successfully")
    else:
        print("Invalid Current PIN")

def transaction_menu(card_number):
    while True:
        show_menu()
        choice = int(input("Enter a number: "))
        if choice == 1:
            balance_enquiry(card_number)
        elif choice == 2:
            withdraw(card_number)
        elif choice == 3:
            deposit(card_number)
        elif choice == 4:
            change_pin(card_number)
        elif choice == 5:
            print("Exiting to main menu...")
            break
        else:
            print("Invalid Choice")
        print("Thanks for Visiting!\n")

while True:
    print("\nWelcome To Ravi's ATM")
    print("Insert Your Card\nPress\n1 for Proceed\n2 for Exit")
    user_input = int(input("Enter a number: "))

    if user_input == 2:
        print("Thank you! Visit Again.")
        break
    elif user_input != 1:
        print("Invalid Input")
        continue

    print("Login Details")
    card_number = input("Enter Your Card Number: ")
    pin = int(input("Enter PIN: "))

    if card_number in cards and cards[card_number][0] == pin:
        print(f"Login Successful With Card: {card_number}")
        transaction_menu(card_number)
    else:
        print("Invalid Card Number or PIN")

    input("Press Enter to continue...")

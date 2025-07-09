card1 = ["A1",1111,50000.00]
card2 = ["A2",2222,60000.00]
card3 = ["A3",3333,70000.00]
card4 = ["A4",4444,80000.00]
while True:
    print("Welcome To Ravi's ATM")
    print("Insert Your Card\nPress\n1 for Proceed\n2 for Exit")
    user1 = int(input("Enter a number: "))
    if user1 not in [1,2]:
        print("Invalid Input")
    elif user1 == 1:
        print("Login Details")
        user2 = input("Enter Your Card Number: ")
        user3 = int(input("Enter PIN: "))
        #Card1
        if user2 == card1[0] and user3 == card1[1]:
            print(f"Login Sucessful With Card:{card1[0]}")
            print("Press\n1 for Balance Enquiry\n2 for Withdraw\n3 for Deposit\n4 for Change Pin\n5 for Exit")
            user4= int(input("Enter a number: "))
            if user4 == 1:
                print(f"Card Number:{card1[0]}")
                print(f"Avaliable Balance:{card1[2]}")
                
            elif  user4 ==2:
                amount = float(input("Enter the Amount: "))
                if amount>0 and amount<=card1[2]:
                    card1[2] -= amount
                    print(f"A1 Debited for Rs.{amount} and Avl Balance Rs.{card1[2]}")
                else:
                    print("Insufficiant Funds")
                
            elif  user4 ==3:
                amount = float(input("Enter the Amount: "))
                if amount>0:
                    card1[2] += amount
                    print(f"A1 Credited for Rs.{amount} and Avl Balance Rs.{card1[2]}")
                else:
                    print("Invalid Input")
            elif user4 == 4:
                current_pin =int(input("Enter Your Current PIN: "))
                if current_pin == card1[1]:
                    updated_pin = int(input("Enter new PIN: "))
                    card1[1] = updated_pin
                    print("PIN Updated")
                else:
                    print("Invalid Current Pin")
            elif user4==5:
                print("Exit")
            print("Thanks for Visting!")

        #Card2
        elif user2 == card2[0] and user3 == card2[1]:
            print(f"Login Sucessful With Card:{card2[0]}")
            print("Press\n1 for Balance Enquiry\n2 for Withdraw\n3 for Deposit\n4 for Change Pin\n5 for Exit")
            user4= int(input("Enter a number: "))
            if user4 == 1:
                print(f"Card Number:{card2[0]}")
                print(f"Avaliable Balance:{card2[2]}")
            elif  user4 ==2:
                amount = float(input("Enter the Amount: "))
                if amount>0 and amount<=card2[2]:
                    card2[2] -= amount
                    print(f"A2 Debited for Rs.{amount} and Avl Balance Rs.{card2[2]}")
                else:
                    print("Insufficiant Funds")
            elif  user4 ==3:
                amount = float(input("Enter the Amount: "))
                if amount>0:
                    card2[2] += amount
                    print(f"A2 Credited for Rs.{amount} and Avl Balance Rs.{card2[2]}")
                else:
                    print("Invalid Input")
            elif user4 == 4:
                current_pin =int(input("Enter Your Current PIN: "))
                if current_pin == card2[1]:
                    updated_pin = int(input("Enter new PIN: "))
                    card2[1] = updated_pin
                    print("PIN Updated")
                else:
                    print("Invalid Current Pin")
            elif user4==5:
                print("Exit")
            print("Thanks for Visting!")
        #Card3
        elif user2 == card3[0] and user3 == card3[1]:
            print(f"Login Sucessful With Card:{card3[0]}")
            print("Press\n1 for Balance Enquiry\n2 for Withdraw\n3 for Deposit\n4 for Change Pin\n5 for Exit")
            user4= int(input("Enter a number: "))
            if user4 == 1:
                print(f"Card Number:{card3[0]}")
                print(f"Avaliable Balance:{card3[2]}")
            elif  user4 ==2:
                amount = float(input("Enter the Amount: "))
                if amount>0 and amount<=card3[2]:
                    card3[2] -= amount
                    print(f"A3 Debited for Rs.{amount} and Avl Balance Rs.{card3[2]}")
                else:
                    print("Insufficiant Funds")
            elif  user4 ==3:
                amount = float(input("Enter the Amount: "))
                if amount>0:
                    card3[2] += amount
                    print(f"A3 Credited for Rs.{amount} and Avl Balance Rs.{card3[2]}")
                else:
                    print("Invalid Input")
            elif user4 == 4:
                current_pin =int(input("Enter Your Current PIN: "))
                if current_pin == card3[1]:
                    updated_pin = int(input("Enter new PIN: "))
                    card3[1] = updated_pin
                    print("PIN Updated")
                else:
                    print("Invalid Current Pin")
            elif user4==5:
                print("Exit")
            print("Thanks for Visting!")

        #Card4
        elif user2 == card4[0] and user3 == card4[1]:
            print(f"Login Sucessful With Card:{card4[0]}")
            print("Press\n1 for Balance Enquiry\n2 for Withdraw\n3 for Deposit\n4 for Change Pin\n5 for Exit")
            user4= int(input("Enter a number: "))
            if user4 == 1:
                print(f"Card Number:{card4[0]}")
                print(f"Avaliable Balance:{card4[2]}")
            elif  user4 ==2:
                amount = float(input("Enter the Amount: "))
                if amount>0 and amount<=card4[2]:
                    card4[2] -= amount
                    print(f"A4 Debited for Rs.{amount} and Avl Balance Rs.{card4[2]}")
                else:
                    print("Insufficiant Funds")
            elif  user4 ==3:
                amount = float(input("Enter the Amount: "))
                if amount>0:
                    card4[2] += amount
                    print(f"A4 Credited for Rs.{amount} and Avl Balance Rs.{card4[2]}")
                else:
                    print("Invalid Input")
            elif user4 == 4:
                current_pin =int(input("Enter Your Current PIN: "))
                if current_pin == card4[1]:
                    updated_pin = int(input("Enter new PIN: "))
                    card4[1] = updated_pin
                    print("PIN Updated")
                else:
                    print("Invalid Current Pin")
            elif user4==5:
                print("Exit")
            print("Thanks for Visting!")    
        else:
            print("Invalid Card Number or PIN")
    user5 = input("Press 'Enter' to Cancel")
    if True:
        continue    
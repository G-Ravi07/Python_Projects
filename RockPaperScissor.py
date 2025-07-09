import random
#Rock = 0, Paper = 1, Scissors = 2
while True:
    com = random.randint(0,2)
    user = int(input("0 for Rock\n1 for Paper\n2 for Scissors\nEnter Your Choice:"))
    if com == 0 and user ==0 or com == 1 and user ==1 or com==2 and user==2:
        print("Draw")
    elif com == 0 and user == 1 or com == 1 and user ==2 or com == 2 and user ==0:
        print("User Won")
    else:
        print("Computer Won")
    choice = int(input("1 to continue\n2 to exit\nEnter your choice:"))
    if choice ==2:
        break

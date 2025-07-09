import random
#Guess a number
com = random.randint(1,100)
count = 0
while True:
    user = int(input("Enter a number between 1 to 100:"))
    count+=1
    if user>com:
        print("Enter a smaller number")
    elif user<com:
        print("Enter a larger number")
    elif user == com:
        print(f"Congrats! You have guessed the number in {count} times")
        break

import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit(Q): ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        if(target - userChoice < 10):
            print("You are close. Guess a slightly bigger one..")
        else:
            print("Your number was too small. Take a bigger guess..")
    else:
        if(userChoice - target < 10):
            print("You are close. Guess a slightly smaller one..")
        else:
            print("Your number was too big. Take a smaller guess..")
print("=====GAME OVER=====")

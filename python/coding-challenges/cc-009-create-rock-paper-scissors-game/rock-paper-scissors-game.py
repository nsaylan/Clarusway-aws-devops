from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

c=0
u=0

user = False

while user == False:
    if c==3:
        print (f"User won {c} time(s) and computer won {u}time(s).Computer has won the game!")
    elif u==3:
        print (f"User won {c} time(s) and computer won {u}time(s).User has won the game!")
    else:
        continue
    user = input("Please enter your weapon: Rock, Paper, Scissors?")
    if user == computer:
        print("tie - no one wins")
    elif user == "Rock":
        if computer == "Paper":
            print("paper beats rock - computer wins")
            c+=1
        else:
            print("rock beats scissors - user wins")
            u+=1
    elif user == "Paper":
        if computer == "Scissors":
            print("scissors beats paper - computer wins")
            c+=1
        else:
            print("scissors beats rock - user wins")
            u+=1
    elif user == "Scissors":
        if computer == "Rock":
            print("rock beats scissors - computer wins")
            c+=1
        else:
            print("scissors beats paper - user wins")
            u+=1
    else:
        print("That's not a valid play. Check your spelling!")
    #user was set to True, but we want it to be False so the loop continues
    user = False
    computer = t[randint(0,2)]
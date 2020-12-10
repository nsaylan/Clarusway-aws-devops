import random 
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock beats scissors \n"
                                +"Paper beats rock \n"
                                +"Scissors beat paper \n"
                                +"If both users choose the same object, it is a tie \n") 
c=0
u=0

while True: 
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
    user = int(input("Please enter your weapon: ")) 
    if c==3:
        print (f"User won {c} time(s) and computer won {u} time(s).Computer has won the game!")
    elif u==3:
        print (f"User won {c} time(s) and computer won {u} time(s).User has won the game!")
     
    
    while user > 3 or user < 1: 
        user = int(input("enter valid input: ")) 
          
    computer = random.randint(1, 3) 
  
    if user == computer:
        print("tie - no one wins")

    elif user == 1:
        if computer == 2:
            print("paper beats rock - computer wins")
            c+=1
        else:
            print("rock beats scissors - user wins")
            u+=1
    elif user == 2:
        if computer == 3:
            print("scissors beats paper - computer wins")
            c+=1
        else:
            print("scissors beats rock - user wins")
            u+=1
    elif user == 3:
        if computer == 1:
            print("rock beats scissors - computer wins")
            c+=1
        else:
            print("scissors beats paper - user wins")
            u+=1
        
          
    ans = input("Do you want to play again? (Y/N)") 
  
  
    if ans == 'n' or ans == 'N': 
        break
      
print("\nThanks for playing") 
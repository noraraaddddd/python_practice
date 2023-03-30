import random

options = ("rock", "paper", "scissors")


 

running = True

while running:
   computer = random.choice(options)
   user = None 
   while user not in options:
    user = input("Choose an option(rock, paper, scissors): ")

   print(f"computer : {computer}")
   print(f"user : {user}")
   
   if user == computer:
     print("It's a tie!")
   elif user == "rock" and computer == "scissors":
     print("You win!")
   elif user == "scissors" and computer == "paper":
     print("you win!")
   elif user == "paper" and computer == "rock":
     print("You win!")
   else:
    print("You lose!")

   if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing :)")

    
    


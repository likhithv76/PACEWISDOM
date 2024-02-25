import random

print("Let's play Rock Paper Scissors")
user = input("Enter the choice? 'r' for Rock , 'p' for Paper and 's' for scissors: ")
computer = random.choice(['r','p','s'])


if ( user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
    print("You won!")

else:
    print("Better luck next time!")
    

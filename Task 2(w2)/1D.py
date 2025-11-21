import random 
options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)
user_choice = input("Enter rock, paper, or scissors: ")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("You lose!")

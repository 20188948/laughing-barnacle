import random 
guess = False 
attempt = 0
play = True
modes = input("would you like to play on easy , medium or hard mode?: ")
modes = modes.lower()
if modes == 'easy':
    random_number = random.randint(1,50)
    print("You are guessing between 1 and 50")
elif modes == 'medium':
    random_number = random.randint(1,100)
    print("You are guessing between 1 and 100")
elif modes == 'hard':
    random_number = random.randint(1,500)
    print("You are guessing between 1 and 500")

player_guess = int(input("Guess a number: "))
while play == True:
    while guess == False:
        if player_guess > random_number:
            print("Too high")
            attempt = attempt + 1 
            player_guess = int(input("Guess again!: "))
        elif player_guess < random_number:
            print("Too low")
            attempt = attempt + 1 
            player_guess = int(input("Guess again!: "))
        #not working 
        elif attempt == 10:
            print("Game over!!!")
            print("It took you",attempt,"many attempts.") 
            break
        elif player_guess == random_number:
            print("Correct!")
            attempt = attempt + 1 
            guess = True
            print("It took you",attempt,"many attempts.")
    play_again = input("Do you want to play again? (Y/N)")
    play_again = play_again.upper()
    if play_again == 'N':
        play = False 





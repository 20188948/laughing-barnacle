import random 
import math
def fruit_guessing_game():
    count = 0
    guess = ["apple", "banana", "cherry", "grape", "orange", "peach", "pear", "plum", "kiwi", "mango"]
    answer=random.choice(guess)
    user_guess =input("Guess a fruit from the list (apple, banana, cherry, grape, orange, peach, pear, plum, kiwi, mango): ")
    while user_guess != answer:
        if user_guess == answer:
            print("Correct! The answer is", answer)
        else:
            user_guess =input("Wrong! Try again: ") 
            count += 1
    print("You've made", count, "guesses.")
def guessing_game():
    number = random.randint(1, 100)
    guess = None
    attempts = 0
    print("Welcome to the Guessing Game! I'm thinking of a number between 1 and 100.")
    
    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
def is_square():
    test=True
    while test==True:
        n=int(input("Enter a number to test if it is a perfect square: "))
        number=math.sqrt(n)
        floor=math.floor(number)
        if floor*floor==n:
            print(n,"is a perfect square")
        else:
            print(n,"is not a perfect square")
def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    user_choice = input("Enter rock, paper, or scissors: ")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")
def wordle():
    # Load words from file
    with open("words_alpha.txt", "r") as file:
        words = file.read().splitlines()

    fiveletter_words = [word for word in words]
    chosen_word = random.choice(fiveletter_words)

    print("Welcome to Wordle! You have 6 attempts to guess the 5-letter word.")

    attempts = 6

    for attempt in range(attempts):
        valid = False
        while not valid:
            guess = input(f"Attempt {attempt + 1}: Enter your 5-letter guess: ").lower()
            if len(guess) == 5 and guess in fiveletter_words:
                valid = True
            else:
                print("Invalid guess. Make sure it's a valid 5-letter word.")

    # Feedback with ANSI colors
        feedback = ""
        for i in range(5):
            if guess[i] == chosen_word[i]:
                feedback += f"\033[92m{guess[i]}\033[0m "  # Green
            elif guess[i] in chosen_word:
                feedback += f"\033[93m{guess[i]}\033[0m "  # Yellow
            else:
                feedback += f"{guess[i]} "  # No color

        print("Feedback:", feedback.strip())

        if guess == chosen_word:
            print(" Congratulations! You guessed the word!")
            break
    else:
        print(f" Out of attempts! The word was: {chosen_word}")
def playing():
    keep_playing = True
    while keep_playing == True:
        answer = input("do you want to keep playing/play? yes or no: ")
        if answer == "no":
            keep_playing = False
        else:
            keep_playing = True
        user_input = input("pick by entering guessing game or fruit game or perfect square or rock paper scissors or wordle  ")
        if user_input == "guessing game":
            guessing_game()
        elif user_input == "fruit game":
            fruit_guessing_game()
        elif user_input == "perfect square":
            is_square()
        elif user_input == "rock paper scissors":
            rock_paper_scissors()
        elif user_input == "wordle":
            wordle()
playing()
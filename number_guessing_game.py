import random

chosen_number = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} to guess the number.")

is_number_guessed = False

def wrongGuess():
    global attempts
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses.")
    else:
        print("Guess again")
        print(f"You have {attempts} attempts left.")


while not is_number_guessed and attempts > 0:
    guessed_number = int(input("Make a guess: "))
    if guessed_number == chosen_number:
        print(f"You got it! the answer was {guessed_number}")
        is_number_guessed = True
    elif guessed_number < chosen_number:
        print("Too low.")
        wrongGuess()
    elif guessed_number > chosen_number:
        print("Too high.")
        wrongGuess()
    else:
        wrongGuess()
from art import logo, vs
import random
from game_data import data

def pick_first_character(account):
    name = account["name"]
    description = account["description"]
    origin = account["country"]
    return f"{name}, a {description}, from {origin}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {pick_first_character(account_a)}")
    print(vs)
    print(f"Against B: {pick_first_character(account_b)}")

    guess = input("Who has more followers? Type 'a' or 'b': ")

    print("\n" * 20)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        should_continue = False
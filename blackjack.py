import sys
import random

def calculate_score(cards):
    score = sum(cards)
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if wants_to_play == "n":
    sys.exit()

user_cards = random.choices(cards, k=2)
computer_cards = random.choices(cards, k=2)

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards are {user_cards}, current score is {user_score}")
print(f"Computer's first card: {computer_cards[0]}")

while user_score < 21:
    action = input("Type 'h' to hit; type 's' to stand: ").lower()
    if action == 'h':
        user_cards.append(random.choice(cards))
        user_score = calculate_score(user_cards)
        print(f"Your cards are {user_cards}, current score is {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score > 21:
            print("You went over. You lose 😭")
            sys.exit()
    elif action == 's':
        break

print(f"Your final hand: {user_cards}, final score: {user_score}")

while computer_score < 17:
    computer_cards.append(random.choice(cards))
    computer_score = calculate_score(computer_cards)

print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

if computer_score > 21:
    print("Dealer bursted! You win 🏆")
elif user_score > 21:
    print("You went over. You lose 😭")
elif user_score > computer_score:
    print("You win 🏆")
elif user_score == computer_score:
    print("It's a draw 😐")
else:
    print("You lose 😢")

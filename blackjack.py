import sys
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if wants_to_play == "n":
    sys.exit()


user_cards = random.choices(cards, k = 2)
current_score = sum(user_cards)
print(f"Your cards are {user_cards}, current score is {current_score}")

computer_starting_cards = random.choices(cards, k = 2)
computer_first_card = computer_starting_cards[0]
computer_total = sum(computer_starting_cards)

print(f"Computer's first card: {computer_first_card}")

get_another_card = input("Type 'h' to hit; type 's' to stand: ").lower()
if get_another_card == "h":

    while get_another_card != "s":
        user_cards.append(random.choice(cards))
        current_score = sum(user_cards)
        print(f"Your cards are {user_cards}, current score is {current_score}")
        print(f"Computer's first card: {computer_first_card}")
        if current_score > 21:
            break
        get_another_card = input("Type 'h' to hit; type 's' to stand: ").lower()

    if current_score > 21:
        print("You went over. You lose 😭")
else:
    print(f"Your final hand: {user_cards}, final score: {current_score}")
    while computer_total <= 16:
        computer_starting_cards.append(random.choice(cards))
        computer_total = sum(computer_starting_cards)
    print(f"Computer's final hand: {computer_starting_cards}, final score: {computer_total}")
    if computer_total > 21:
        print("Dealer bursted! you win 🏆")
    else:
        if current_score <= 21:
            if computer_total < current_score:
                print("You win 🏆")
            elif computer_total == current_score:
                print("It's a draw 😐")
            else:
                print("You lose 😢")
        else:
            print("You exceeded 21. You lose 😔")
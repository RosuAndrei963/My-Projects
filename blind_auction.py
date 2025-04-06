bidding_history = {

}

people_left = True

while people_left == True:
    user_name = input("Type your name: ")
    user_bid  = int(input("Type your bid: $"))
    peopleleft = input("Are there any people left? yes/no ").lower()
    bidding_history[user_name] = user_bid
    if peopleleft == "no":
        people_left = False
    else:
        print("\n" * 25)

final = 0
winner = ""
for name, bid in bidding_history.items():
    if bid > final:
        final = bid
        winner = name

print(f"The winner is {winner}, with a bid of {bid}")
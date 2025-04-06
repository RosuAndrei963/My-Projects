import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

h = int(input("Welcome to Rock Paper Scissors! Choose yours; 1 for rock, 2 for paper and 3 for scissors:"))
if h < 4 and h > 0:
    if h == 1:
        print(rock)
    elif h == 2:
        print(paper)
    elif h == 3:
        print(scissors)

    c = random.randint(1,3)
    print("computer chose: ")
    if c == 1:
        print(rock)
    elif c == 2:
        print(paper)
    elif c == 3:
        print(scissors)
    if c == h:
        print("Draw")
    elif h == 1 and c == 2:
        print("you lost")
    elif h == 1 and c == 3:
        print("you won!")
    elif h == 2 and c == 1:
        print("you won!")
    elif h == 2 and c == 3:
        print("you lost")
    elif h == 3 and c == 1:
        print("you lost")
    elif h == 3 and c == 2:
        print("you won!")
else:
    print("Typed a wrong int; you lose")
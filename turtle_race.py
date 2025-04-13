import random
from turtle import Screen, Turtle

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Bet which turtle will win the race: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

if user_bet:
    race_on = True

y_coord = -150
for turtle_index in range(6):
    timmy = Turtle("turtle")
    timmy.color(colors[turtle_index])
    timmy.penup()
    y_coord += 50
    timmy.goto(x=-230, y=y_coord)
    turtles.append(timmy)

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The winning turtle is {winning_turtle}")
            else:
                print(f"You've lost! The winning turtle is {winning_turtle}")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()

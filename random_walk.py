from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
screen = Screen()
colormode(255)
timmy.pensize(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def random_direction():
    directions = [0, 90, 180, 270]
    heading = random.choice(directions)
    timmy.setheading(heading)

for i in range(100):
    random_direction()
    timmy.color(random_color())
    timmy.forward(25)

screen.exitonclick()

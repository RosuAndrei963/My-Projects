from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
screen = Screen()
colormode(255)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(120):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(3)


screen.exitonclick()

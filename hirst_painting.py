import turtle
from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
screen = Screen()
screen.setup(width=800, height=800)
colormode(255)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy.penup()
y = -250
timmy.goto(-250, y)



for i in range(10):
    for j in range(10):
        timmy.color(random_color())
        timmy.dot(20)
        timmy.forward(50)
    y += 50
    timmy.goto(-250, y)
turtle.hideturtle()    

screen.exitonclick()

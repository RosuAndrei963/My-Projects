from turtle import Turtle, Screen, colormode
import random


timmy = Turtle()
screen = Screen()
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

angle = 360
number_of_angles = 3


for i in range(8):
    a = angle / number_of_angles
    timmy.color(random_color())
    for j in range(number_of_angles):
        timmy.forward(100)
        timmy.right(a)
    number_of_angles += 1
    print(number_of_angles)

screen.exitonclick()

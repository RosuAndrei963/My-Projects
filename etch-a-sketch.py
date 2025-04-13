from turtle import Screen, Turtle

# Create the turtle and screen
timmy = Turtle()
screen = Screen()

# Movement functions
def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_right():
    timmy.right(10)

def turn_left():
    timmy.left(10)

def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

# Key bindings
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear_drawing, "c")

# Close on click
screen.exitonclick()

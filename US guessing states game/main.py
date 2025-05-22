import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
df.to_string()

user_guesses = []
score = 0
title = "Guess the State"


while len(user_guesses) < 50:
    input_answer = screen.textinput(title=title, prompt="Type Another State").title().strip()

    if input_answer == "Exit":
        missing_states = [state for state in df.state if state not in user_guess]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if input_answer in df.state.values:
        score += 1
        user_guesses.append(input_answer)
        title = f"Correct States: {score}/50"
        state_cor = df[df.state == input_answer]
        x = int(state_cor.x.values[0])
        y = int(state_cor.y.values[0])
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(x, y)
        text.write(input_answer, align="center", font=("Arial", 8, "normal"))


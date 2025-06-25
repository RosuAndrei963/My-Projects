import tkinter
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANG_NAME_FONT = ("ariel", 40, "italic")
WORD_FONT = ("ariel", 60, "bold")
current_word = {}
word_list = {}

# -------------------------- MECHANISM/BACKEND -------------------------- #

try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = df.to_dict(orient="records")


def new_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(word_list)
    canvas.itemconfig(text_language, text="German", fill="black")
    canvas.itemconfig(text_content, text=current_word["German"], fill="black")
    canvas.itemconfig(card_bg, image=front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(text_language, text="English", fill="white")
    canvas.itemconfig(text_content, text=current_word["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_image)

def remove_card():
    word_list.remove(current_word)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()


# -------------------------- UI -------------------------- #

window = tkinter.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = tkinter.PhotoImage(file="./images/card_front.png")
back_image = tkinter.PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_image)
text_language = canvas.create_text(400, 150, text="", fill="black", font=LANG_NAME_FONT)
text_content = canvas.create_text(400, 263, text="", fill="black", font=WORD_FONT)
new_word()
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
right_image = tkinter.PhotoImage(file="./images/right.png")
unknown_button = tkinter.Button(image=wrong_image, highlightthickness=0, bd=0, command=new_word)
unknown_button.grid(row=1, column=0)
known_button = tkinter.Button(image=right_image, highlightthickness=0, bd=0, command=remove_card)
known_button.grid(row=1, column=1)





window.mainloop()
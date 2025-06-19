import tkinter
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    """Generate a random password and copy it to clipboard."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(3, 5))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    pass_list = pass_letters + pass_symbols + pass_numbers

    random.shuffle(pass_list)

    password = "".join(pass_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    # WARNING: Storing passwords in plain text is not secure.
    # This is for educational purposes only.
    # Do NOT use this in real applications without encryption.
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if not website or not email or not password:
        messagebox.showerror(title="Alert", message="You forgot to add something")
    else:
        valid = messagebox.askokcancel(title="Website", message=f"Add {email} and {password}?")
        if valid:
            with open("data.txt", "a") as d:
                d.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, tkinter.END)
                pass_entry.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Passwords")
window.config(padx=25, pady=25)

canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file="lock image.png")
canvas.create_image(100, 100, image = image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_entry = tkinter.Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, "email")

pass_label = tkinter.Label(text="Password: ")
pass_label.grid(column=0, row=3)

pass_entry = tkinter.Entry(width=22)
pass_entry.grid(column=1, row=3)

gen_pass_button = tkinter.Button(text="Generate Password", command=generate_pass)
gen_pass_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add password", width=36, command=add_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
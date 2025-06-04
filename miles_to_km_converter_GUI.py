import tkinter

FONT = ("Arial", 24, "bold")

window = tkinter.Tk()
window.title("Mile to Km converter")
window.minsize(width=350, height=200)

blank = tkinter.Label(text="Enter: ", font=FONT)
blank.grid(column=0, row=0)

input = tkinter.Entry(width = 10)
input.grid(column=1, row=0)

miles = tkinter.Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)

label = tkinter.Label(text="is equal to", font=FONT)
label.grid(column=0, row=1)

kmv = tkinter.Label(text="-", font=FONT)
kmv.grid(column=1, row=1)

km = tkinter.Label(text="Km", font=FONT)
km.grid(column=2, row=1)


def changetext():
    inputValue = float(input.get())
    inputValue *= 1.609
    kmv.config(text = round(inputValue, 2))


button = tkinter.Button(text = "Convert", command = changetext)
button.grid(column=1, row=2)






window.mainloop()

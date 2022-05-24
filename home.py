from tkinter import *
from tkinter import ttk


def next_page():
    window.destroy()
    import main

YELLOW = "#f7f5dd"

window = Tk()
window.title("home page")
window.config(padx=100, pady=100, bg=YELLOW)

label = Label(window, text="welcome to home page")
label.pack()

button = Button(text="1hr", command=next_page)
button.pack()

if __name__ == '__main__':
    window.mainloop()

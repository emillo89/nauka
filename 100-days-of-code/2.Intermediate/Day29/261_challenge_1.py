from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white",highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.pack()


window.mainloop()
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white",highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", bg="white")
website.grid(column=0, row=1)
email = Label(text="Email/Username:", bg="white")
email.grid(column=0, row=2)
password = Label(text="Password", bg="white")
password.grid(column=0, row=3)

web_entry = Entry()
web_entry.grid(column=1, row=1, columnspan=2, sticky="WE")
email_entry = Entry()
email_entry.grid(column = 1, row=2, columnspan=2, sticky="WE")
password_entry = Entry(width=33)
password_entry.grid(column=1,row=3)

generate_button = Button(text="Generate Password", bg="white")
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", bg="white")
add_button.grid(column=1, row=4, columnspan=2, sticky="WE")

window.mainloop()
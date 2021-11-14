import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    nr_symbols = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    nr_numbers = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pas = nr_letters + nr_symbols + nr_numbers
    random.shuffle(pas)
    password = ''.join(pas)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():

    your_web = web_entry.get()
    your_email = email_entry.get()
    your_password = password_entry.get()

    if len(your_web) == 0 or len(your_password) == 0:
        info = messagebox.showinfo(title=website, message="Please make sure you haven't left any fields empty. ")
    else:
        is_ok = messagebox.askokcancel(title=your_web, message=f"These are the details entered: \nEmail: {your_email}"
                                                               f"\nPassword: {your_password} \nIs it ok to save?")
        if is_ok:
            #save a web, email and password
            with open("data.txt", mode="a") as file:
                file.write(f"{your_web} | {your_email} | {your_password}\n")
                #when you write your web and password, delete your things
                web_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
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

#Cursor place
web_entry.focus()
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="WE")

#Default email
email_entry.insert(0, "emil@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)


generate_button = Button(text="Generate Password", bg="white", command = generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="WE")

window.mainloop()

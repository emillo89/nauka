from tkinter import *
import random, string

#  pyperclip - modul pozwalajacy kopiowanie i wklejanie do schowka
import pyperclip


root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Password generator')

Label(root, text = 'password generator', font = 'arial 25 bold').pack()
Label(root,text = 'Dataflair', font = 'arial 15 bold').pack(side = BOTTOM)

pass_label = Label(root, text = 'password length', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_= 8, to_= 32, textvariable = pass_len, width = 15).pack()

pass_str = StringVar()

def generator():
    password = ''

    for x in range(0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice((string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
    pass_str.set(password)


Button(root, text = 'Generate password', command = generator).pack(pady = 5)
Entry(root, textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'copy to clipboard', command = Copy_password).pack(pady = 5)




root.mainloop()
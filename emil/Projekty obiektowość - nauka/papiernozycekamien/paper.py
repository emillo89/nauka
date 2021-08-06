import random
from tkinter import *

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock,Paper,Scissors')
root.config(bg='seashell3')

#heading
Label(root,text = 'paper, rock, scissors', font = 'arial 20 bold', bg = 'seashell2').pack()

# user choice
user_take = StringVar()
Label(root,text = 'choose any one: rock, paper, scissors', font = ' arial 15 bold',bg = 'seashell2' ).place(x = 20, y = 70)
Entry(root,font = 'arial 15', textvariable = user_take,bg = 'antiquewhite2').place(x = 90, y = 130)

# computer choice

comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set("Wybraliscie to samo")
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('Przegrales. komputer wybral paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set("wygrałes, komputer wybral nozyczki")
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('Przegrales, komputer wybrał nozyczki')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('wygrales, komputer wybral kamien')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('Przegrales, komputer wybral kamien')
    elif user_pick == ' scissors' and comp_pick =='paper':
        Result.set('Wygrales, komputer wybral papier')
    else:
        Result.set('Wybierz jedno z : papier, nozyce, kamien')

#   fun  to reset
def Reset():
    Result.set("")
    user_take.set("")

# fun to exit
def Exit():
    root.destroy()


Entry(root, font = 'arial 10 bold', textvariable = Result, bg='antiquewhite2', width = 50 ).place(x = 25, y = 250)
Button(root,font = 'arial 10 bold', text = 'Play', padx = 5, bg ='seashell4', command = play ).place(x=150, y = 190)
Button(root, font= 'arial 10 bold', text = 'Reset', padx = 5, bg ='seashell4', command = Reset).place(x = 70, y = 310)
Button(root, font ='arial 10 bold', text = 'Exit', padx = 5, bg ='seashell4' , command = Exit).place(x= 230, y =310)
root.mainloop()






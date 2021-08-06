from tkinter import *
# gtts - google text to speech - konwersja textu do audio
from gtts import gTTS
# playsound - do uruchomienia audio
from playsound import playsound

root = Tk()
root.geometry('350x350')
root.configure(bg = 'ghost white')
root.title('Text to speech')

Label(root, text = 'text to speech', font = 'arial 20 bold',bg = 'white smoke').pack()
Label(root, text = 'DataFlair', font = 'arial 15 bold', bg = 'white smoke').pack(side = 'bottom')

Msg = StringVar()
Label(root, text = 'Enter text', font = 'arial 15 bold', bg = 'white smoke').place(x=20, y = 60)
entry_field = Entry(root, textvariable = Msg, width = '50')
entry_field.place(x=20, y=100)


def text_to_speech():
    Message = Msg.get()
    #  lub mozemy Message zrobic w inny sposob
    # Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Dataflair.mp3')
    playsound('DataFlair.mp3')

def Reset():
    Msg.set('')

def Exit():
    root.destroy()

Button(root, text = "PLAY" , font = 'arial 15 bold', command = text_to_speech, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =140)

root.mainloop()
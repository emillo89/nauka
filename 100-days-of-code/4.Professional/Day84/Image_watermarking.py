from tkinter.messagebox import showinfo

from PIL import Image
import tkinter as tk
from tkinter import filedialog

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title = 'Watermark App'
        self.geometry('300x300')
        self.add_widgets()


    def add_widgets(self):
        self.quit_widget()
        self.add_images()

    def add_images(self):
        self.image_button = tk.Button(text='Add new images', command=self.add_images_command)
        self.image_button.grid(column=0, row=0)

    def quit_widget(self):
        self.quit_button = tk.Button(text='Quit', command=self.quit_command)
        self.quit_button.grid(column=0, row=1)

    def add_images_command(self):



        self.filenames = filedialog.askopenfilenames(title='Open a file',
                                                   initialdir='/',
                                                   filetypes=(('jpeg', '*.jpg'),('.png', '*.png'), ('all files', '*.*')),
                                                   )
        showinfo(title='Selected File',
                 message=self.filenames)

    def quit_command(self):
        self.destroy()



app = App()

app.mainloop()
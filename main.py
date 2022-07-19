import sqlite3
import subprocess
import tkinter as tk
from tkinter import ttk, LEFT, filedialog
import xml.dom.minidom
import pyperclip

from page_one import *

LARGE_FONT = ('Verdana', 18)
NORMAL_FONT = ('Verdana', 12)
SMALL_FONT = ('Verdana', 8)


def open_db():
    file = 'my_database.db'
    subprocess.call(['open', file])


class DbManagement(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        db = sqlite3.connect('my_database.db')
        cursor = db.cursor()

        header = []

        tk.Tk.wm_title(self, 'Database Management for Accuracy Test')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Save Settings', command=lambda: print("Done"))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=quit)
        menubar.add_cascade(label='File', menu=filemenu)
        '''secondmenu = tk.Menu(menubar, tearoff=1)
        secondmenu.add_command(label='ex', command=lambda: qf())'''
        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        def buttons():
            button1 = tk.Button(self, text='Go home and create new project',
                                command=lambda: self.show_frame(PageOne))
            button1.pack(side=LEFT)
            button2 = tk.Button(self, text='Open Database',
                                command=lambda: open_db())
            button2.pack(side=LEFT)
            button3 = tk.Button(self, text='Exit',
                                command=quit)
            button3.pack(side=LEFT)

        buttons()

        for F in (PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(column=1, row=1, sticky="NSEW")

        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def entries_labels():
            label = tk.Label(self, text='Generate XML file to be used in Geomagic Control X', font=LARGE_FONT)
            label.grid(row=0, column=0, pady=10, padx=10, sticky="NSEW", columnspan=3)

        entries_labels()


class Database(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.db_path = 'my_database.db'


app = DbManagement()
app.geometry('480x720')
app.minsize(480, 720)
app.maxsize(480, 720)
app.mainloop()

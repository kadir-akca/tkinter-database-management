import sqlite3
import subprocess
import tkinter as tk
from tkinter import ttk, LEFT, filedialog
import xml.dom.minidom
import pyperclip

from page_one import PageOne
from page_three import PageThree
from page_two import PageTwo

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

        # ---- Buttons ----- #
        btn_go_page_1 = tk.Button(self, text='First Page',
                                  command=lambda: click_first_page())
        btn_open_db = tk.Button(self, text='Open Database',
                                command=lambda: open_db())
        btn_go_page_2 = tk.Button(self, text='Second Page',
                                  command=lambda: click_second_page())
        btn_go_page_3 = tk.Button(self, text='Third Page',
                            command=lambda: click_third_page())

        btn_quit = tk.Button(self, text='Exit',
                             command=quit)

        btn_go_page_1.pack(side=LEFT)
        btn_go_page_2.pack(side=LEFT)
        btn_go_page_3.pack(side=LEFT)
        btn_open_db.pack(side=LEFT)
        btn_quit.pack(side=LEFT)

        my_frames = (PageOne, PageTwo, PageThree)

        for F in my_frames:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(column=0, row=0, sticky="NSEW")

        #self.show_frame(PageOne)



        def click_first_page():
            self.show_frame(PageOne)
            btn_go_page_1.config(state='disabled')
            btn_go_page_2.config(state='normal')
            btn_go_page_3.config(state='disabled')

        def click_second_page():
            self.show_frame(PageTwo)
            btn_go_page_1.config(state='normal')
            btn_go_page_2.config(state='disabled')
            btn_go_page_3.config(state='normal')

        def click_third_page():
            self.show_frame(PageThree)
            btn_go_page_1.config(state='normal')
            btn_go_page_2.config(state='normal')
            btn_go_page_3.config(state='disabled')

        click_first_page()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = DbManagement()
app.geometry('480x720')
app.minsize(480, 720)
app.maxsize(480, 720)
app.mainloop()

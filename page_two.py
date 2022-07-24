import sqlite3
import subprocess
import tkinter as tk
from tkinter import ttk, LEFT, filedialog, END
import xml.dom.minidom
import pyperclip

LARGE_FONT = ('Verdana', 18)
NORMAL_FONT = ('Verdana', 12)
SMALL_FONT = ('Verdana', 8)


class PageTwo(tk.Frame):
    experience_id_2 = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        experience_id_l = tk.Label(self, text="ExperienceID:")
        experience_id_l.grid(row=1, column=0)

        results_l = tk.Label(self, text='Test Results\n _____________________________', font=LARGE_FONT)
        results_l.grid(row=2, column=0, columnspan=3, sticky='NSEW')

        self.experience_id_2 = tk.Entry(self)
        self.experience_id_2.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=2, sticky="NSEW")

        copy = tk.Button(self, command=lambda: self.copy_to_clipboard(), text='Copy to Clipboard')
        copy.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=2, sticky="NSEW")

    @staticmethod
    def insert_experience_id_l(expid):
        PageTwo.experience_id_2.insert(0, expid)

    def copy_to_clipboard(self):
        pyperclip.copy(str(self.experience_id_2))



import sqlite3
import subprocess
import tkinter as tk
from tkinter import ttk, LEFT, filedialog, END
import xml.dom.minidom


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        experience_id_l = tk.Label(self, text="ExperienceID:")
        experience_id_l.grid(row=1, column=0)

        experience_id = tk.Entry(self)
        experience_id.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=2, sticky="NSEW")
        # experience_id.insert(0, self.exxx)
        experience_id.config(state='disabled')

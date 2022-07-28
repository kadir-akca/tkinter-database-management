import os
import random
import sys
from tkinter import Tk

import pyperclip


def copy(x):
    pyperclip.copy(x)


def paste():
    x = pyperclip.paste()
    return x

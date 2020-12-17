import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("boom")
root.geometry('700x700')

frame = LabelFrame(root, padx=5, pady=2)
frame.grid(padx=10, pady=5, columnspan=4, column=0, row=0, sticky="nw")

root.mainloop()

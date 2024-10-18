from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Sistema Financeiro')

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

name = StringVar()
name_entry = ttk.Entry(mainframe, width=7, textvariable=name)
name_entry.grid(column=2, row=1, sticky=(W, E))

root.mainloop()
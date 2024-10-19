from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Sistema Financeiro')

def printName(*args):
    msg = ttk.Label(mainframe, text="Bem vinda " + name.get()).grid(column=2, row=2)

mainframe = ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

name = StringVar()
name_entry = ttk.Entry(mainframe, width=7, textvariable=name)
name_entry.grid(column=2, row=1, sticky=(W, E))


enter = ttk.Button(mainframe, text="Enter", command=printName)
enter.grid(column=2, row=3)

for a in root.grid_slaves():
    print(a)

root.mainloop()
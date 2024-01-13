from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor

def openFile():
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text File", ".txt"), ("All Files", ".*")])

    if file:
        content = file.read()
        text.delete(1.0, END)
        text.insert(END, content)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text File", ".txt"), ("All Files", ".*")])

    if file:
        filetext = text.get(1.0, END)
        file.write(filetext)
        file.close()

def exitApp():
    screen.destroy()

def chooseColor():
    color = askcolor(title="Color Chooser")[1]
    text.config(foreground=color)

def saveCtrl(event):
    if event.state == 4 and event.keysym.lower() == 's':
        print("Ctrl + S pressed")

screen = Tk()
title = "Swift Edit"

screen.title(title)

menubar = Menu(screen)
screen.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
colorMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
menubar.add_cascade(label="Color", menu=colorMenu)

fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Exit", command=exitApp)

colorMenu.add_command(label="Choose Color", command=chooseColor)

text = Text(screen)
text.config(font=("arial", 30))
text.pack(expand=YES, fill=BOTH)

screen.mainloop()
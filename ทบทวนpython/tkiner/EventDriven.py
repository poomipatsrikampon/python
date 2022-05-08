from tkinter import Button, Tk
from tkinter import *

def leftClickButton(event):
    print("Left Click!!")


def doubleClickButton(event):
    print("double Click!!")

main = Tk()
button = Button(main,text= "My Button !!")
button.pack()
button.bind('<Button-1>',leftClickButton)
button.bind('<Double-3>',doubleClickButton)
main.mainloop()
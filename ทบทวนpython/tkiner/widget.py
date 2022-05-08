from tkinter import *

def sayHelloWorld():
    print("Hello World")

main_window = Tk()
button = Button(main_window,text= "Click me",command=sayHelloWorld)
button.place(x=50,y=20)
main_window.mainloop()
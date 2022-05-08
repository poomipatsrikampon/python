from tkinter import *

def sayHelloWorld():
    print("Hello World")

main_window = Tk()
button = Button(main_window,text= "Click me1",command=sayHelloWorld).grid(row=0,column=1)
button2 = Button(main_window,text= "Click me2",command=sayHelloWorld).grid(row=1)
button3 = Button(main_window,text= "Click me3",command=sayHelloWorld).grid(row=2)
main_window.mainloop()
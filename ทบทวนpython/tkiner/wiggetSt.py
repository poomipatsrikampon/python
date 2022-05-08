from tkinter import *

def sayHelloWorld():
    print("Hello World")

main_window = Tk()
button = Button(main_window,text= "Click me",command=sayHelloWorld)
button.place(x=50,y=20)
main_window.mainloop()

main_window2 = Tk()
button1 = Button(main_window2,text= "Click me",command=sayHelloWorld)
button1.place(x=50,y=20)
main_window2.mainloop()

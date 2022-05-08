from cProfile import label
from cgitb import text
import imp
from tkinter import *

def BMI_calculate(event):
    weight = int(textbox_weight.get())
    height = int(textbox_height.get())/100
    label_BMI.configure(text=weight/(height**2))
    

main_window = Tk()

label_height = Label(main_window, text="ส่วนสูง (cm) ")
textbox_height = Entry(main_window)
label_weight = Label(main_window, text="น้ำหนัก (Kg) ")
textbox_weight = Entry(main_window)
label_BMI = Label(main_window, text="BMI")

label_height.grid(row=0,column=0)
textbox_height.grid(row=0,column=1)
label_weight.grid(row=1,column=0)
textbox_weight.grid(row=1,column=1)
label_BMI.grid(row=2,column=0)

calculate_button = Button(main_window,text= "คำนวณ")
calculate_button.bind('<Button-1>',BMI_calculate)
calculate_button.grid(row=3)


main_window.mainloop()

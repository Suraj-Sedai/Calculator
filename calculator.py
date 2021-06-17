import tkinter
from tkinter import*

root = Tk()
root.title("Standard Calculator")
root.iconbitmap('C:/Users/suraj/OneDrive/Documents/Coding/images/icon.ico')

e = Entry(root, width=38, borderwidth=1)
e.grid(row=0, column=0, columnspan=4)

#e.insert(0, "")

def button_click(number):
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math=="addition":
        e.insert(0, f_num + int(second_number))

    if math=="subtraction":
        e.insert(0, f_num - int(second_number))

    if math=="multiplaction":
        e.insert(0, f_num * int(second_number))

    if math=="division":
        e.insert(0, f_num / int(second_number))

    if math=="percent":
        e.insert(0, (f_num / 100) * int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplaction"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_percent():
    first_number = e.get()
    global f_num
    global math
    math = "percent"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_back():
    e.delete(1, END)

button_1 = Button(root, text="1", padx=30, pady=20, relief=GROOVE, borderwidth=1,font=("Courier",12), command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click(0))
button_dot = Button(root, text=".", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command=lambda: button_click())
button_percent = Button(root, text="%", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), command= button_percent)
button_add = Button(root, text="+", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), fg="#2c3e50", command= button_add)
button_equal = Button(root, text="=", padx=30, pady=50, relief=GROOVE,borderwidth=1,font=("Courier",12), fg="#fff", bg="#2c3e50", command= button_equal)
button_clear = Button(root, text="AC", padx=26, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), fg="#2c3e50", command= button_clear)
button_back = Button(root, text="C", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), fg="#2c3e50", command= button_back)
2
button_subtract = Button(root, text="-", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), fg="#2c3e50", command= button_subtract)
button_multiply = Button(root, text="*", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), fg="#2c3e50", command= button_multiply)
button_division = Button(root, text="/", padx=30, pady=20, relief=GROOVE,borderwidth=1,font=("Courier",12), fg="#2c3e50", command= button_division)

#put the button on the screen

button_back.grid(row=1, column=0)
button_division.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_clear.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_equal.grid(row=4, column=3, rowspan=2)

button_percent.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)

root.mainloop()

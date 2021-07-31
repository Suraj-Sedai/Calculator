from tkinter import* 
root = Tk()
root.title("Calclator")
root.iconbitmap("") 

e = Entry(root, font = ("Verdana", 22))
e.grid(row=0, column=0, columnspan=4, ipady=20)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str(number))

def button_tclose():
    e.delete(0, END)

def button_close():
    e.delete(0, END)    

def button_back():
    e.delete(0, END)

def button_plus():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math=="add":
        e.insert(0, f_num + int(second_number))
    if math=="sub":
        e.insert(0, f_num - int(second_number))
    if math=="mul":
        e.insert(0, f_num * int(second_number))
    if math=="div":
        e.insert(0, f_num / int(second_number))
    if math=="per":
        e.insert(0, f_num  * (int(second_number)/100))    

def button_per():
    first_number = e.get()
    global f_num
    global math
    math = "per"
    f_num = int(first_number)
    e.delete(0, END)

button_1 = Button(root, text="1", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(1))
button_2 = Button(root, text="2", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(2))
button_3 = Button(root, text="3", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(3))
button_4 = Button(root, text="4", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(4))
button_5 = Button(root, text="5", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(5))
button_6 = Button(root, text="6", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(6))
button_7 = Button(root, text="7", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(7))
button_8 = Button(root, text="8", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(8))
button_9 = Button(root, text="9", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(9))
button_0 = Button(root, text="0", font = ("Verdana", 12), pady=10, border=0, command= lambda: button_click(0))
button_plus = Button(root, text="+", font = ("Verdana", 12), pady=10, border=0, command= button_plus)
button_sub = Button(root, text="-", font = ("Verdana", 12), pady=10, border=0, command= button_sub)
button_mul = Button(root, text="×", font = ("Verdana", 12), pady=10, border=0, command= button_mul)
button_equal = Button(root, text="=", font = ("Verdana", 12), pady=10, border=0, command= button_equal)
button_div = Button(root, text="/", font = ("Verdana", 12), pady=10, border=0, command= button_div)
button_per = Button(root, text="%", font = ("Verdana", 12), pady=10, border=0, command= button_per)
button_del = Button(root, text=".", font = ("Verdana", 12), pady=10, border=0, command= button_click, state=DISABLED)
button_back = Button(root, text="ⓧ", font = ("Verdana", 12), pady=10, border=0, command= button_back)
button_clear = Button(root, text="C", font = ("Verdana", 12), pady=10, border=0, command= button_close,  state=DISABLED)
button_tclear = Button(root, text="CE", font = ("Verdana", 12), pady=10, border=0, command= button_tclose,  state=DISABLED)

button_tclear.grid(row=1, column=0)
button_clear.grid(row=1, column=1)
button_back.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_6.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_4.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_plus.grid(row=4, column=3)

button_per.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_del.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

root.mainloop()

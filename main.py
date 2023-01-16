from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from compute import *

class window(Tk):
	def __init__(self):
		super().__init__()
		Style(theme="darkly")
		self.style = ttk.Style(self)

def write(c):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, current + c)

def clear():
    screen.delete(0, END)

def delete():
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, current[:-1])

def equals():
    expression = screen.get()
    result = compute(expression)
    screen.delete(0, END)
    screen.insert(0, result)

root = window()

root.geometry("390x280")
root.title("Calcolatrice")

screen = Entry(root, width=50)

button_1 = Button(root, text="1", command=lambda:write("1"))
button_2 = Button(root, text="2", command=lambda:write("2"))
button_3 = Button(root, text="3", command=lambda:write("3"))
button_4 = Button(root, text="4", command=lambda:write("4"))
button_5 = Button(root, text="5", command=lambda:write("5"))
button_6 = Button(root, text="6", command=lambda:write("6"))
button_7 = Button(root, text="7", command=lambda:write("7"))
button_8 = Button(root, text="8", command=lambda:write("8"))
button_9 = Button(root, text="9", command=lambda:write("9"))
button_0 = Button(root, text="0", command=lambda:write("0"))

button_add = Button(root, text="+", command=lambda:write("+"))
button_subtract = Button(root, text="-", command=lambda:write("-"))
button_multiply = Button(root, text="x", command=lambda:write("x"))
button_divide = Button(root, text="/", command=lambda:write("/"))

button_equals = Button(root, text="=", command=equals)

button_open = Button(root, text="(", command=lambda:write("("))
button_closed = Button(root, text=")", command=lambda:write(")"))

button_point = Button(root, text=".", command=lambda:write("."))
button_sign = Button(root, text="+/_", command=lambda:write("_"))

button_del = Button(root, text="<-", command=delete)
button_clear = Button(root, text="Clear", command=clear)

button_1.grid(row=3, column=0, ipadx=15, ipady=15)
button_2.grid(row=3, column=1, ipadx=15, ipady=15)
button_3.grid(row=3, column=2, ipadx=15, ipady=15)
button_4.grid(row=2, column=0, ipadx=15, ipady=15)
button_5.grid(row=2, column=1, ipadx=15, ipady=15)
button_6.grid(row=2, column=2, ipadx=15, ipady=15)
button_7.grid(row=1, column=0, ipadx=15, ipady=15)
button_8.grid(row=1, column=1, ipadx=15, ipady=15)
button_9.grid(row=1, column=2, ipadx=15, ipady=15)
button_0.grid(row=4, column=1, ipadx=15, ipady=15)

button_add.grid(row=1, column=3, ipadx=15, ipady=15)
button_subtract.grid(row=2, column=3, ipadx=17, ipady=15)
button_multiply.grid(row=3, column=3, ipadx=16, ipady=15)
button_divide.grid(row=4, column=3, ipadx=17, ipady=15)

button_equals.grid(row=4, column=4, columnspan=2, ipadx=44, ipady=15)

button_open.grid(row=3, column=4, ipadx=15, ipady=15)
button_closed.grid(row=3, column=5, ipadx=15, ipady=15)

button_point.grid(row=4, column=2, ipadx=16, ipady=15)
button_sign.grid(row=4, column=0, ipadx=9, ipady=15)

button_del.grid(row=2, column=4, columnspan=2, ipadx=42, ipady=15)
button_clear.grid(row=1, column=4, columnspan=2, ipadx=33, ipady=15)

screen.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

root.mainloop()
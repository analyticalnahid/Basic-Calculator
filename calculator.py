# Importing Required Library
from tkinter import *

# Creating Tkinter Objects
win = Tk()

# Global Variable
expression = ""

# Fitting Window
win.geometry("312x324")
win.resizable(0, 0)

# Setting Title 
win.title("Calculator (Nahidul)")


# Function which make program dynamic

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


# Textinput
input_text = StringVar()
# Frame For Textinput 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame For Button
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()


# Creating All Button

def button(text, width, command):
    return Button(btns_frame, text=text, fg="black", width=width, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=command)


button("C", 32, lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
button("/", 10, lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

button("7", 10, lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
button("8", 10, lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
button("9", 10, lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
button("*", 10, lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

button("4", 10, lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
button("5", 10, lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
button("6", 10, lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
button("-", 10, lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

button("1", 10, lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
button("2", 10, lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
button("3", 10, lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
button("+", 10, lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

button("0", 21, lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
button(".", 10, lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
button("=", 10, lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)


win.mainloop()

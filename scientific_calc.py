import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")

expression = ""

# Update display
def press(val):
    global expression
    expression += str(val)
    equation.set(expression)

# Clear
def clear():
    global expression
    expression = ""
    equation.set("")

# Backspace
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Calculate safely
def calculate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Scientific functions
def apply_func(func):
    global expression
    try:
        value = float(expression)
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log10(value)
        elif func == "sqrt":
            result = math.sqrt(value)
        equation.set(str(result))
        expression = str(result)
    except:
        equation.set("Error")

# Display
equation = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, justify="right")
entry.grid(row=0, column=0, columnspan=5)

# Button function
def btn(text, row, col, cmd):
    tk.Button(root, text=text, width=5, height=2, command=cmd).grid(row=row, column=col)

# Row 1
btn("C",1,0, clear)
btn("⌫",1,1, backspace)
btn("(",1,2, lambda: press("("))
btn(")",1,3, lambda: press(")"))
btn("^",1,4, lambda: press("**"))

# Row 2
btn("sin",2,0, lambda: apply_func("sin"))
btn("cos",2,1, lambda: apply_func("cos"))
btn("tan",2,2, lambda: apply_func("tan"))
btn("log",2,3, lambda: apply_func("log"))
btn("√",2,4, lambda: apply_func("sqrt"))

# Row 3
btn("7",3,0, lambda: press("7"))
btn("8",3,1, lambda: press("8"))
btn("9",3,2, lambda: press("9"))
btn("/",3,3, lambda: press("/"))
btn("π",3,4, lambda: press(str(math.pi)))

# Row 4
btn("4",4,0, lambda: press("4"))
btn("5",4,1, lambda: press("5"))
btn("6",4,2, lambda: press("6"))
btn("*",4,3, lambda: press("*"))
btn("e",4,4, lambda: press(str(math.e)))

# Row 5
btn("1",5,0, lambda: press("1"))
btn("2",5,1, lambda: press("2"))
btn("3",5,2, lambda: press("3"))
btn("-",5,3, lambda: press("-"))
btn("%",5,4, lambda: press("%"))

# Row 6
btn("0",6,0, lambda: press("0"))
btn(".",6,1, lambda: press("."))
btn("=",6,2, calculate)
btn("+",6,3, lambda: press("+"))

root.mainloop()

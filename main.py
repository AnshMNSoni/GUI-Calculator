# Basic Calculator:

import tkinter as tk

FONT = ('Comic Sans', 16, 'normal')
THEME = '#3F6075'
SP_THEME = '#A03C3C'


# Function to update the expression in the entry box
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)


# Function to clear the entry box
def button_clear():
    global expression
    expression = ""
    input_text.set("")
    

# Function to evaluate the expression and update the entry box with the result
def button_equal():
    global expression
    
    # replacing ^ -> **
    new_exp = [items.replace("^", "**") for items in expression]
    
    expression = ""
    for item in new_exp:
        expression += item
    
    
    # Error Handling:
    try:
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)
        expression = result
    except:
        input_text.set("Syntax Error")
        expression = ""


# Main Tkinter window
window = tk.Tk()
window.title("Calculator")
window.config()
window.geometry("750x650")
expression = ""
input_text = tk.StringVar()


# Entry widget to display the expression and result
input_frame = tk.Frame(window)
input_frame.pack(expand=True)


input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 38, 'bold'), bd=10, insertwidth=4, width=44, justify='right', bg=THEME, fg='white')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


# Frame for buttons
btns_frame = tk.Frame(window)
btns_frame.pack()


# First row
clear = tk.Button(btns_frame, text="C", width=10, height=3, font=FONT, bg=SP_THEME, bd= 10, command=lambda: button_clear()).grid(row=0, column=0)
modulus = tk.Button(btns_frame, text="%", width=10, height=3, font=FONT, bd= 10, command=lambda: button_click("%")).grid(row=0, column=1)
exp = tk.Button(btns_frame, text="^", width=10, height=3, font=FONT, bd= 10, command=lambda: button_click("^")).grid(row=0, column=2)
divide = tk.Button(btns_frame, text="/", font=FONT, width=10, height=3, bd= 10, command=lambda: button_click("/")).grid(row=0, column=3)


# Second row
seven = tk.Button(btns_frame, text="7", width=10, height=3, font=FONT, bd= 10, command=lambda: button_click(7)).grid(row=1, column=0)
eight = tk.Button(btns_frame, text="8", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click(8)).grid(row=1, column=1)
nine = tk.Button(btns_frame, text="9", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click(9)).grid(row=1, column=2)
multiply = tk.Button(btns_frame, text="*", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click("*")).grid(row=1, column=3)


# Third row
four = tk.Button(btns_frame, text="4", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click(4)).grid(row=2, column=0)
five = tk.Button(btns_frame, text="5", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click(5)).grid(row=2, column=1)
six = tk.Button(btns_frame, text="6", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click(6)).grid(row=2, column=2)
subtract = tk.Button(btns_frame, text="-", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click("-")).grid(row=2, column=3)


# Fourth row
one = tk.Button(btns_frame, text="1", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click(1)).grid(row=3, column=0)
two = tk.Button(btns_frame, text="2", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click(2)).grid(row=3, column=1)
three = tk.Button(btns_frame, text="3", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click(3)).grid(row=3, column=2)
add = tk.Button(btns_frame, text="+", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click("+")).grid(row=3, column=3)


# Fifth row
zero = tk.Button(btns_frame, text="0", width=24, height=3,font=FONT, bd= 10, command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2)
point = tk.Button(btns_frame, text=".", width=10, height=3,font=FONT, bd= 10, command=lambda: button_click(".")).grid(row=4, column=2)
equals = tk.Button(btns_frame, text="=", width=10, height=3, font=FONT, bg=SP_THEME, bd= 10, command=lambda: button_equal()).grid(row=4, column=3)


# Run the main event loop
window.mainloop()
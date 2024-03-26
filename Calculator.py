import tkinter as tk

# Calculator window and title
window = tk.Tk()
window.title("Calculator")

# Global variables to hold the values taken in by the buttons and the equation to calculate when pressing the equals button
values = tk.StringVar()
equation = ""

def click(num):
    '''
    The function runs when a button is clicked.
    '''
    global equation
    # Adding the button clicked to the equation
    equation = equation + str(num)
    # Displaying the button value on the screen
    values.set(equation)

def clear_screen():
    '''
    This function runs when the 'Clear' button is clicked.
    '''
    global equation
    # Setting the equation back to empty
    equation = ""
    # Clearing the display screen
    values.set(equation)

def calculate():
    '''
    This function calculates the full equation when the '=' button is clicked and displays it on the screen.
    '''
    values.set(eval(equation))

# The display for the numbers and equations
display = tk.Label(window, height=2, anchor='w', bg="#FDF5E6", foreground="black", textvariable=values)
display.pack(side='top', expand='yes', fill='x')

# Frame for the calculator buttons
button_frame = tk.Frame(window, height=350, width=330)
button_frame.pack()

# Drawing the calculator buttons
one = tk.Button(button_frame, text="1", width=8, height=2, command=lambda:click(1))
two = tk.Button(button_frame, text="2", width=8, height=2, command=lambda:click(2))
three = tk.Button(button_frame, text="3", width=8, height=2, command=lambda:click(3))
plus = tk.Button(button_frame, text="+", width=8, height=2, command=lambda:click('+'))

four = tk.Button(button_frame, text="4", width=8, height=2, command=lambda:click(4))
five = tk.Button(button_frame, text="5", width=8, height=2, command=lambda:click(5))
six = tk.Button(button_frame, text="6", width=8, height=2, command=lambda:click(6))
minus = tk.Button(button_frame, text="-", width=8, height=2, command=lambda:click('-'))

seven = tk.Button(button_frame, text="7", width=8, height=2, command=lambda:click(7))
eight = tk.Button(button_frame, text="8", width=8, height=2, command=lambda:click(8))
nine = tk.Button(button_frame, text="9", width=8, height=2, command=lambda:click(9))
multiply = tk.Button(button_frame, text="*", width=8, height=2, command=lambda:click('*'))

zero = tk.Button(button_frame, text="0", width=12, height=2, command=lambda:click(0))
point = tk.Button(button_frame, text=".", width=8, height=2, command=lambda:click('.'))
divide = tk.Button(button_frame, text="/", width=8, height=2, command=lambda:click('/'))

equals = tk.Button(button_frame, text="=", width=16, height=2, command=lambda:calculate())
clear = tk.Button(button_frame, text="Clear", width=8, height=2, command=lambda:clear_screen())

# Placement of calculator buttons
one.grid(row=0, column=0, sticky='NSEW')
two.grid(row=0, column=1, sticky='NSEW')
three.grid(row=0, column=2, sticky='NSEW')
plus.grid(row=0, column=3, sticky='NSEW')

four.grid(row=1, column=0, sticky='NSEW')
five.grid(row=1, column=1, sticky='NSEW')
six.grid(row=1, column=2, sticky='NSEW')
minus.grid(row=1, column=3, sticky='NSEW')

seven.grid(row=2, column=0, sticky='NSEW')
eight.grid(row=2, column=1, sticky='NSEW')
nine.grid(row=2, column=2, sticky='NSEW')
multiply.grid(row=2, column=3, sticky='NSEW')

zero.grid(row=3, column=0, columnspan=2, sticky='NSEW')
point.grid(row=3, column=2, sticky='NSEW')
divide.grid(row=3, column=3, sticky='NSEW')

equals.grid(row=4, column=0, columnspan=3, sticky='NSEW')
clear.grid(row=4, column=3, sticky='NSEW')

# Configure buttons so they shrink with window
button_frame.columnconfigure(0, weight=1)
button_frame.rowconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.rowconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.rowconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)
button_frame.rowconfigure(3, weight=1)
button_frame.rowconfigure(4, weight=1)

if __name__ == "__main__":
    # Run window
    window.mainloop()
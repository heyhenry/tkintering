import tkinter as tk

result = ''
working_equation = ''
equation = []

root = tk.Tk()

# get the user input values to create the equation
def get_equation(mouse_event, val):
    global equation
    # global working_equation
    # to show the value the user has inputted
    user_input_var.set(val)
    # update the equation list
    equation.append(val)
    print_equation()

# remove the last user input from the equation
def backspace_an_input():
    global equation
    # remove the last element in the equation list
    equation.pop()
    print_equation()

# clear the whole equation
def clear_all_equation():
    global equation
    # clear the whole equation list
    equation.clear()
    print_equation()

# show the equation and its result
def calculate_equation():
    print(equation)
    global result
    for i in equation:
        result += i
    print(eval(result))

# displays the equation in realtime within the app
def print_equation(*args):
    global working_equation
    # clean slate the working_equation variable for the latest equation list (with no previous versions attached)
    working_equation = ''
    # append the latest equation to the working_equation variable
    for i in equation:
        working_equation += i
    # set the entry's showcasing variable with the latest equation updates
    display_equation_var.set(str(working_equation))
    
display_equation_var = tk.StringVar()
user_input_var = tk.StringVar()

button_params = {'font': ('helvetica', 24), 'width': 5}

display_equation_field = tk.Entry(root, textvariable=display_equation_var, font=('helvetica', 18))
display_equation_field.grid(row=0, columnspan=5)

input_field = tk.Entry(root, textvariable=user_input_var, font=('helvetica', 35))
input_field.grid(row=1, columnspan=5)

number_seven = tk.Button(root, text='7', **button_params)
number_eight = tk.Button(root, text='8', **button_params)
number_nine = tk.Button(root, text='9', **button_params)
division_operator = tk.Button(root, text='/', **button_params)
addition_operator= tk.Button(root, text='+', **button_params)
number_seven.grid(row=2, column=0)
number_eight.grid(row=2, column=1)
number_nine.grid(row=2, column=2)
division_operator.grid(row=2, column=3)
addition_operator.grid(row=2, column=4)

number_four = tk.Button(root, text='4', **button_params)
number_five = tk.Button(root, text='5', **button_params)
number_six = tk.Button(root, text='6', **button_params)
multiplier_operator = tk.Button(root, text='X', **button_params)
empty_one = tk.Button(root, text='', **button_params, state='disabled')
number_four.grid(row=3, column=0)
number_five.grid(row=3, column=1)
number_six.grid(row=3, column=2)
multiplier_operator.grid(row=3, column=3)
empty_one.grid(row=3, column=4)

number_one = tk.Button(root, text='1', **button_params)
number_two = tk.Button(root, text='2', **button_params)
number_three = tk.Button(root, text='3', **button_params)
subtract_operator = tk.Button(root, text='-', **button_params)
empty_two = tk.Button(root, text='', **button_params, state='disabled')
number_one.grid(row=4, column=0)
number_two.grid(row=4, column=1)
number_three.grid(row=4, column=2)
subtract_operator.grid(row=4, column=3)
empty_two.grid(row=4, column=4)

decimal_point = tk.Button(root, text='.', **button_params)
number_zero = tk.Button(root, text='0', **button_params)
equals_sign = tk.Button(root, text='=', **button_params, command=calculate_equation)
clear_sign = tk.Button(root, text='C', **button_params, command=backspace_an_input)
all_clear_sign = tk.Button(root, text='AC', **button_params, command=clear_all_equation)
decimal_point.grid(row=5, column=0)
number_zero.grid(row=5, column=1)
equals_sign.grid(row=5, column=2)
clear_sign.grid(row=5, column=3)
all_clear_sign.grid(row=5, column=4)

number_seven.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '7'))
number_eight.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '8'))
number_nine.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '9'))
number_four.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '4'))
number_five.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '5'))
number_six.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '6'))
number_one.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '1'))
number_two.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '2'))
number_three.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '3'))
number_zero.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '0'))

division_operator.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '/'))
addition_operator.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '+'))
multiplier_operator.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '*'))
subtract_operator.bind("<Button-1>", lambda mouse_event: get_equation(mouse_event, '-'))

display_equation_var.trace_add('write', print_equation)

root.mainloop()
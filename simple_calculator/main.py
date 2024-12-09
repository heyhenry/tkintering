import tkinter as tk

root = tk.Tk()

user_input_var = tk.StringVar()

button_params = {'font': ('helvetica', 24), 'width': 5}

input_field = tk.Entry(root, textvariable=user_input_var, font=('helvetica', 35))
input_field.grid(row=0, columnspan=5)

number_seven = tk.Button(root, text='7', **button_params)
number_eight = tk.Button(root, text='8', **button_params)
number_nine = tk.Button(root, text='9', **button_params)
division_operator = tk.Button(root, text='/', **button_params)
addition_operator= tk.Button(root, text='+', **button_params)
number_seven.grid(row=1, column=0)
number_eight.grid(row=1, column=1)
number_nine.grid(row=1, column=2)
division_operator.grid(row=1, column=3)
addition_operator.grid(row=1, column=4)

number_four = tk.Button(root, text='4', **button_params)
number_five = tk.Button(root, text='5', **button_params)
number_six = tk.Button(root, text='6', **button_params)
multiplier_operator = tk.Button(root, text='X', **button_params)
empty_one = tk.Button(root, text='', **button_params, state='disabled')
number_four.grid(row=2, column=0)
number_five.grid(row=2, column=1)
number_six.grid(row=2, column=2)
multiplier_operator.grid(row=2, column=3)
empty_one.grid(row=2, column=4)

number_one = tk.Button(root, text='1', **button_params)
number_two = tk.Button(root, text='2', **button_params)
number_three = tk.Button(root, text='3', **button_params)
subtract_operator = tk.Button(root, text='-', **button_params)
empty_two = tk.Button(root, text='', **button_params, state='disabled')
number_one.grid(row=3, column=0)
number_two.grid(row=3, column=1)
number_three.grid(row=3, column=2)
subtract_operator.grid(row=3, column=3)
empty_two.grid(row=3, column=4)

decimal_point = tk.Button(root, text='.', **button_params)
number_zero = tk.Button(root, text='0', **button_params)
equals_sign = tk.Button(root, text='=', **button_params)
clear_sign = tk.Button(root, text='C', **button_params)
all_clear_sign = tk.Button(root, text='AC', **button_params)
decimal_point.grid(row=4, column=0)
number_zero.grid(row=4, column=1)
equals_sign.grid(row=4, column=2)
clear_sign.grid(row=4, column=3)
all_clear_sign.grid(row=4, column=4)

root.mainloop()
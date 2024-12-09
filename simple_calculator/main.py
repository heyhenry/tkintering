import tkinter as tk

root = tk.Tk()

user_input_var = tk.StringVar()

input_field = tk.Entry(root, textvariable=user_input_var, font=('helvetica', 24))
input_field.grid(row=0, columnspan=4)

number_seven = tk.Button(root, text='7', font=('helvetica', 24))
number_eight = tk.Button(root, text='8', font=('helvetica', 24))
number_nine = tk.Button(root, text='9', font=('helvetica', 24))
division_operator = tk.Button(root, text='/', font=('helvetica', 24))
number_seven.grid(row=1, column=0)
number_eight.grid(row=1, column=1)
number_nine.grid(row=1, column=2)
division_operator.grid(row=1, column=3)

number_four = tk.Button(root, text='4', font=('helvetica', 24))
number_five = tk.Button(root, text='5', font=('helvetica', 24))
number_six = tk.Button(root, text='6', font=('helvetica', 24))
multiplier_operator = tk.Button(root, text='X', font=('helvetica', 24))
number_four.grid(row=2, column=0)
number_five.grid(row=2, column=1)
number_six.grid(row=2, column=2)
multiplier_operator.grid(row=2, column=3)

number_one = tk.Button(root, text='1', font=('helvetica', 24))
number_two = tk.Button(root, text='2', font=('helvetica', 24))
number_three = tk.Button(root, text='3', font=('helvetica', 24))
subtract_operator = tk.Button(root, text='-', font=('helvetica', 24))
number_one.grid(row=3, column=0)
number_two.grid(row=3, column=1)
number_three.grid(row=3, column=2)
subtract_operator.grid(row=3, column=3)

decimal_point = tk.Button(root, text='.', font=('helvetica', 24))
number_zero = tk.Button(root, text='0', font=('helvetica', 24))
equals_sign = tk.Button(root, text='=', font=('helvetica', 24))
clear_sign = tk.Button(root, text='C', font=('helvetica', 24))
decimal_point.grid(row=4, column=0)
number_zero.grid(row=4, column=1)
equals_sign.grid(row=4, column=2)
clear_sign.grid(row=4, column=3)



root.mainloop()
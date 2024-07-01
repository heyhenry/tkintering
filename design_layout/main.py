import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

# central top
main_title = tk.Label(root, text='Main Title Here')

# left side
left_subtitle = tk.Label(root, text='Left Sub Title')
lst_box = tk.Listbox(root)

# right side
first_btn = tk.Button(root, text='First')
second_btn = tk.Button(root, text='Second')
third_btn = tk.Button(root, text='Third')

main_title.grid(row=0, columnspan=2)

left_subtitle.grid(row=1, column=0)
lst_box.grid(row=2, rowspan=3, column=0)

first_btn.grid(row=2, column=1)
second_btn.grid(row=3, column=1)
third_btn.grid(row=4, column=1)

root.mainloop()
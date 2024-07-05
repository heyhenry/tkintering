import tkinter as tk


root = tk.Tk()
root.title('Design Concept #2')

main_screen = tk.Frame(root)
main_screen.pack()

# top center
title_screen = tk.Frame(main_screen, background='red', height=50, width=300)
title_screen.grid(columnspan=3)
title_lbl = tk.Label(title_screen, text='Hello World!')
title_lbl.pack()

# left side
entries_screen = tk.Frame(main_screen, background='green', height=200, width=100)
entries_screen.grid(rowspan=3)
entries_lb = tk.Listbox(entries_screen)
entries_lb.pack()

# middle
buttons_screen = tk.Frame(main_screen, background='yellow', height=200, width=100)
buttons_screen.grid(row=1, column=1)
add_entry = tk.Button(buttons_screen, text='Add Entry')
update_entry = tk.Button(buttons_screen, text='Update Entry')
delete_entry = tk.Button(buttons_screen, text='Delete Entry')
add_entry.grid(row=0, column=0)
update_entry.grid(row=1, column=0)
delete_entry.grid(row=2, column=0)

# right side
stats_screen = tk.Frame(main_screen, background='blue', height=200, width=100)
stats_screen.grid(row=1, column=2)
books_reading = tk.Label(stats_screen, text='Books Reading: ')
books_reading_num = tk.Label(stats_screen, text='3')
books_to_read = tk.Label(stats_screen, text='Books to Read: ')
books_to_read_num = tk.Label(stats_screen, text='23')
books_read = tk.Label(stats_screen, text='Books Read: ')
books_read_num = tk.Label(stats_screen, text='67')
books_reading.grid(row=0, column=0)
books_reading_num.grid(row=0, column=1)
books_to_read.grid(row=1, column=0)
books_to_read_num.grid(row=1, column=1)
books_read.grid(row=2, column=0)
books_read_num.grid(row=2, column=1)

root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title('GUI Layout Example')

# # Main frames
# top_center_frame = tk.Frame(root)
# top_center_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

# left_frame = tk.Frame(root, width=200, height=300, bg='green')
# left_frame.grid(row=1, column=0, sticky="nsew")

# middle_frame = tk.Frame(root, width=200, height=300, bg='yellow')
# middle_frame.grid(row=1, column=1, sticky="nsew")

# right_frame = tk.Frame(root, width=200, height=300, bg='blue')
# right_frame.grid(row=1, column=2, sticky="nsew")

# # Widgets in top_center_frame
# top_label = tk.Label(top_center_frame, text='Top Center Frame')
# top_label.pack(fill='x', padx=10, pady=10)

# # Widgets in left_frame
# listbox = tk.Listbox(left_frame)
# listbox.pack(padx=10, pady=10, fill='both', expand=True)

# # Widgets in middle_frame
# middle_buttons = [
#     tk.Button(middle_frame, text='Button 1'),
#     tk.Button(middle_frame, text='Button 2'),
#     tk.Button(middle_frame, text='Button 3')
# ]

# for i, button in enumerate(middle_buttons):
#     button.grid(row=i, column=0, padx=10, pady=10, sticky="ew")

# # Configure column weight for middle_frame to evenly distribute space
# middle_frame.columnconfigure(0, weight=1)

# # Widgets in right_frame
# right_buttons = [
#     tk.Button(right_frame, text='Button A'),
#     tk.Button(right_frame, text='Button B'),
#     tk.Button(right_frame, text='Button C')
# ]

# for i, button in enumerate(right_buttons):
#     button.grid(row=i, column=0, padx=10, pady=10, sticky="ew")

# # Configure column weight for right_frame to evenly distribute space
# right_frame.columnconfigure(0, weight=1)

# # Configure row and column weights for root to make frames resizeable
# root.grid_rowconfigure(1, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)

# root.mainloop()

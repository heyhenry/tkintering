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
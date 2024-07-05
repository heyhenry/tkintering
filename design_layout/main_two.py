import tkinter as tk


root = tk.Tk()
root.title('Design Concept #2')

main_screen = tk.Frame(root)

# top center
title_screen = tk.Frame(main_screen, background='red', height=50, width=300)

# left side
entries_screen = tk.Frame(main_screen, background='green', height=200, width=100)

# middle
buttons_screen = tk.Frame(main_screen, background='yellow', height=200, width=100)

# right side
stats_screen = tk.Frame(main_screen, background='blue', height=200, width=100)

main_screen.pack()
title_screen.grid(row=0, columnspan=3)
entries_screen.grid(row=1, column=0)
buttons_screen.grid(row=1, column=1)
stats_screen.grid(row=1, column=2)

root.mainloop()
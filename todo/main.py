import tkinter as tk

root = tk.Tk()
root.title('To Do App.')
root.geometry('1000x600')

tasks = tk.Listbox(root)
tasks_scrollbar = tk.Scrollbar(root)
tasks.config(yscrollcommand=tasks_scrollbar.set, width=70, height=30)
tasks_scrollbar.config(command=tasks.yview)

tasks.place(y=50, x=10)
tasks_scrollbar.place(y=50, x=432, width=20, height=480)

for vals in range(100):
    tasks.insert('end', vals)

root.mainloop()
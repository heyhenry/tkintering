# a simple todo app
import tkinter as tk

root = tk.Tk()
root.title('To Do App.')
root.geometry('800x600')
# task input
# add task button

# list added tasks
tasks_listbox_title = tk.Label(root, text='To Do Tasks:', font=(24))
tasks_listbox_title.place(y=50, x=80)

tasks_listbox = tk.Listbox(root)
tasks_listbox.place(y=80, x=30, width=200, height=300)

tasks_listbox_scrollbar = tk.Scrollbar(root)

# remove task

# display selected task
# mark task as done

# clear all button

root.mainloop()
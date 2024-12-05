# a simple todo app
import tkinter as tk

root = tk.Tk()
root.title('To Do App.')
root.geometry('800x600')

task_var = tk.StringVar()

# task input
task_enter_title = tk.Label(root, text='Enter Task:', font=(24))
task_enter_title.place(y=50, x=300)

task_enter_prompt = tk.Entry(root, textvariable=task_var, font=(24))
task_enter_prompt.place(y=50, x=400, width=300)
# add task button
task_add_button = tk.Button(root, text='Add Task')
task_add_button.place(y=48, x=710)

# listbox for added tasks
tasks_listbox_title = tk.Label(root, text='To Do Tasks:', font=(24))
tasks_listbox_title.place(y=50, x=80)

tasks_listbox = tk.Listbox(root)
tasks_listbox.place(y=80, x=30, width=200, height=300)

tasks_listbox_scrollbar = tk.Scrollbar(root)
tasks_listbox_scrollbar.place(y=80, x=230, height=300)

# linking the listbox and scrollbar with eachother
tasks_listbox.config(yscrollcommand=tasks_listbox_scrollbar.set)
tasks_listbox_scrollbar.config(command=tasks_listbox.yview)

# remove task
remove_task_button = tk.Button(root, text='Remove Task')
remove_task_button.config(font=(24))
remove_task_button.place(y=400, x=75)

# clear all button
clear_all_button = tk.Button(root, text='Clear All Tasks')
clear_all_button.config(font=(24))
clear_all_button.place(y=450, x=70)

# display selected task
# mark task as done



root.mainloop()
import tkinter as tk
import json
import os
from task import Task

savefile = 'tasks_save.json'
tasks_dict = {}

root = tk.Tk()
root.title('To Do App.')
root.geometry('500x800')

task_var = tk.StringVar()
task_check_var = tk.IntVar()
selected_task_var = tk.StringVar()

def load_tasks():
    if os.path.exists(savefile):
        with open(savefile, 'r') as file:
            data = json.load(file)
            for task_name, task_info in data.items():
                tasks_dict[task_name] = Task(task_info['task_name'], task_info['task_status'])

# customised serializer for json
def custom_serializer(obj):
    if isinstance(obj, Task):
        return {
            "task_name": obj.task_name,
            "task_status": obj.task_status
        }
    return obj

# populate the task list(todos)
def populate_tasks_list():
    load_tasks()
    for i in tasks_dict.keys():
        tasks.insert('end', i)

# add task to the todo list
def add_task():
    tasks.insert('end', task_var.get())

# display selected task
def display_task(mouse_event):
    for i in tasks.curselection():
        # display the selected task's name
        selected_task.config(text=tasks.get(i))
        # display the correct task status via the checkbutton
        task_check_var.set(tasks_dict[tasks.get(i)].task_status)
        # update the selected task var's value
        selected_task_var.set(tasks.get(i))

# remove selected task
def remove_task():
    for i in tasks.curselection():
        tasks.delete(i)

# update status of a task if checkbutton has a different value than what's saved
def update_task_status(mouse_event):
    if task_check_var.get() != tasks_dict[selected_task_var.get()].task_status:
        tasks_dict[selected_task_var.get()].task_status = task_check_var.get()
        print(tasks_dict[selected_task_var.get()].task_status)

task_subtitle = tk.Label(root, text='Enter Task:', font=(18))
task_entry = tk.Entry(root, textvariable=task_var, font=(18))
submit_task = tk.Button(root, text='Add Task', command=add_task)

task_subtitle.place(y=50, x=30)
task_entry.place(y=50, x=120, width=270)
submit_task.place(y=47, x=400)

tasks = tk.Listbox(root)
tasks_scrollbar = tk.Scrollbar(root)
tasks.config(yscrollcommand=tasks_scrollbar.set, width=70, height=30)
tasks_scrollbar.config(command=tasks.yview)

tasks.place(y=100, x=30)
tasks_scrollbar.place(y=100, x=452, width=20, height=480)

selected_task_subtitle = tk.Label(root, text='Selected Task:', font=(24))
selected_task = tk.Label(root, font=(24), wraplength=300)
task_checkbox = tk.Checkbutton(root, text='Completed', variable=task_check_var, onvalue=1, offvalue=0, font=(18))
remove_task_button = tk.Button(root, text='Remove Task', command=remove_task)

selected_task_subtitle.place(y=600, x=200)
selected_task.place(y=680, x=250, anchor='center', width=300, height=100)
task_checkbox.place(y=600, x=30)
remove_task_button.place(y=595, x=400)

# interact with the list in the todo list and display selected task in the task display section 
tasks.bind('<<ListboxSelect>>', lambda mouse_event: display_task(mouse_event))
task_checkbox.bind('<ButtonRelease-1>', lambda mouse_event: update_task_status(mouse_event))

populate_tasks_list()

root.mainloop()
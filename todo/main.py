# a simple todo app
import tkinter as tk
import json
import os
from task import Task

savefile = 'tasks_save.json'
tasks_list = {}

# load saved data of tasks
def load_saved_tasks():
    if os.path.exists(savefile):
        with open(savefile, 'r') as file:
            save_data = json.load(file)
            for task_name, task_info in save_data.items():
                tasks_list[task_name] = Task(task_info['task_name'], task_info['task_status'])

# created a customised serailizer for json parsing
def custom_serializer(obj):
    if isinstance(obj, Task):
        return {
            "Task Name": obj.task_name,
            "Task Status": obj.task_status
        }
    return obj

load_saved_tasks()

root = tk.Tk()
root.title('To Do App.')
root.geometry('800x600')

task_var = tk.StringVar()
task_check_var = tk.IntVar()

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
selected_task_title = tk.Label(root, text='Task Name:', font=(24))
selected_task_title.place(y=120, x=350)

selected_task_name = tk.Label(root, text='Deep Clean Bedroom', font=(24)) # <-- temp hardcoded text
selected_task_name.place(y=120, x=450)

# mark task as done
selected_task_checkbutton = tk.Checkbutton(root, text='Task Completed', variable=task_check_var, onvalue=1, offvalue=0, font=(24))
selected_task_checkbutton.place(y=180, x=400)

root.mainloop()
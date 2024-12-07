# a simple todo app
import tkinter as tk
import json
import os
from task import Task

savefile = 'tasks_save.json'
tasks_list = {}

# load saved data of tasks
def load_saved_tasks():
    # check to see if the save file exists
    if os.path.exists(savefile):
        # open the found save file
        with open(savefile, 'r') as file:
            # load the json data into a variable
            save_data = json.load(file)
            # loop through the json data and insert into the local tasks list dictionary
            for task_name, task_info in save_data.items():
                tasks_list[task_name] = Task(task_info['task_name'], task_info['task_status'])

# created a customised serailizer for json parsing
def custom_serializer(obj):
    # json format for the task object
    if isinstance(obj, Task):
        return {
            "task_name": obj.task_name,
            "task_status": obj.task_status
        }
    return obj

# update the save file for tasks
def update_savefile():
    # create the json object for the save file
    save_data = json.dumps(tasks_list, indent=4, default=custom_serializer)
    # write the new json data to the save file
    with open(savefile, 'w') as outfile:
        outfile.write(save_data)

load_saved_tasks()

root = tk.Tk()
root.title('To Do App.')
root.geometry('800x600')

# load saved tasks to the listbox
def load_tasks_to_listbox():
    # loop through the existing tasks via their key (task names)
    for task_name in tasks_list.keys():
        # add each existing task to the listbox
        tasks_listbox.insert('end', task_name)

# create a task
def create_task():
    # added the new task to the existing tasks list dictionary
    tasks_list[task_var.get()] = Task(task_var.get(), 'Uncompleted')
    # update the save file to reflect the addition of the new task
    update_savefile()

# add a task to the listbox
def add_task():
    task_error_message.config(text='')
    if validate_new_task():
        # add the task to the listbox
        tasks_listbox.insert('end', task_var.get())
        # create the task
        create_task()

# check if task has an appropriate string length
def validate_new_task():
    # ensure the length of the task is not too long
    if len(task_var.get()) > 26:
        task_error_message.config(text='Too many characters.')
        return False
    # ensure that the user has not only entered an 'empty' task
    elif len(task_var.get()) * ' ' == task_var.get():   
        task_error_message.config(text='White spaces only not allowed.')
        return False
    return True

# remove task from the listbox
def remove_task():
    task_name = ''
    for i in tasks_listbox.curselection():
        # update the task_name variable's value with selected task
        task_name = tasks_listbox.get(i)
        # delete the selected task from the listbox
        tasks_listbox.delete(i)
    # delete the selected task from the tasks list dictionary
    del tasks_list[task_name]
    # update the save file to reflect the removal of the selected task
    update_savefile()

# clear all existing tasks
def clear_all_tasks():
    # find out how many tasks exists
    total_tasks_count = tasks_listbox.size()
    # delete all the tasks via  (first to last)
    tasks_listbox.delete(0, total_tasks_count)
    # clear the whole tasks list dictionary
    tasks_list.clear()    
    # update the save file 
    update_savefile()

def update_task_status():
    task_name = ''
    for i in tasks_listbox.curselection():
        task_name = tasks_listbox.get(i)
    if task_check_var.get() == 1:
        tasks_list[task_name].task_status = 'Completed'
    else:
        tasks_list[task_name].task_status = 'Uncompleted'
    update_savefile()

def display_selected_task_info(mouse_event):
    task_name = ''
    for i in tasks_listbox.curselection():
        task_name = tasks_listbox.get(i)
    selected_task_name.config(text=task_name)
    if tasks_list[task_name].task_status == 'Completed':
        task_check_var.set(1)
    else:
        task_check_var.set(0)

task_var = tk.StringVar()
task_check_var = tk.IntVar()

# task input
task_enter_title = tk.Label(root, text='Enter Task:', font=(24))
task_enter_title.place(y=50, x=300)

task_enter_prompt = tk.Entry(root, textvariable=task_var, font=(24))
task_enter_prompt.place(y=50, x=400, width=300)

# error message prompt
task_error_message = tk.Label(root, foreground='red', font=(24))
task_error_message.place(y=70, x=400)

# add task button
task_add_button = tk.Button(root, text='Add Task', command=add_task)
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
remove_task_button = tk.Button(root, text='Remove Task', command=remove_task)
remove_task_button.config(font=(24))
remove_task_button.place(y=400, x=75)

# clear all button
clear_all_button = tk.Button(root, text='Clear All Tasks', command=clear_all_tasks)
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

# functions to be run at startup
load_tasks_to_listbox()

# bindings
tasks_listbox.bind("<<ListboxSelect>>", lambda mouse_event: display_selected_task_info(mouse_event))

root.mainloop()
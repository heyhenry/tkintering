import tkinter as tk

root = tk.Tk()
root.title('To Do App.')
root.geometry('500x800')

task_var = tk.StringVar()
task_check_var = tk.IntVar()

task_subtitle = tk.Label(root, text='Enter Task:', font=(18))
task_entry = tk.Entry(root, textvariable=task_var, font=(18))
submit_task = tk.Button(root, text='Add Task')

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
selected_task = tk.Label(root, text='jasdfkljasdklfjaklsdjflkajdfklajsdfkljaklsdfjkljasdfkljasdklfjaklsdjflkajdfklajsdfkljaklsdfjkljasdfkljasdklfjaklsdjflkajdfklajsdfkljaklsdfjkljasdfkljasdklfjaklsdjflkajdfklajsdfkljaklsdfjkljasdfkljasdklfjaklsdjflkajdfklajsdfkljaklsdfjkl', font=(24), wraplength=300)
task_checkbox = tk.Checkbutton(root, text='Completed', variable=task_check_var, onvalue=1, offvalue=0, font=(18))
remove_task = tk.Button(root, text='Remove Task')

selected_task_subtitle.place(y=600, x=200)
selected_task.place(y=680, x=250, anchor='center', width=300, height=100)
task_checkbox.place(y=600, x=30)
remove_task.place(y=595, x=400)

root.mainloop()
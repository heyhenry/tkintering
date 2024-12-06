# considerations:
- update ui to a cleaner, minimalistic and simple one

# to implement:
- Validation to restrict length of inputted task
- Create task object for saving purposes (task_name = 'Clean bedroom', task_status = 'Completed' / 'Incompleted')
- Create task dictionary to store saved tasks data
- Create savefile for tasks
- Implement load save file function
- Implement update save file function
- Implement custom serializer function
- Implement remove task function (and update the save file)
- Implement clear all tasks function (and save an empty save file)
- Update save file if checkbutton's state is changed and does not reflect the current savefile
- Display added/saved tasks to the listbox
- Display selected task's name and task status (via text saying either Completed or Incompleted and checkbox reflects text)
# Resources used: 
# creating listboxes: https://www.geeksforgeeks.org/python-tkinter-listbox-widget/
# centering home title: https://stackoverflow.com/questions/70974175/with-tkinter-grid-method-i-want-to-center-the-labels 
# creating a json file: https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
# creating custom json serializer: https://howtodoinjava.com/python-json/custom-class-serialization/
# closing popup window: https://www.geeksforgeeks.org/how-to-close-a-window-in-tkinter/
# to erase file contents: https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python

import tkinter as tk
import json
import os

# entry class obj to store each entry
class Entry:
    def __init__(self, title, type, chapsread, readstat):
        self.title = title
        self.type = type
        self.chapsread = chapsread
        self.readstat = readstat

    # def __str__(self):
    #     return self.title

entries = {}
storage_filename = 'entries.save'

# read and add existing entries found in save file to entries dictionary
def load_entries():

    # check if file exists
    if os.path.exists(storage_filename):

        # reads file
        with open(storage_filename, 'r') as file:
            
            # loads json file data
            entry_data = json.load(file)
            
            # populates dictionary entries with existing entries found in json save file
            for entry_title, entry_info in entry_data.items():
                entries[entry_title] = Entry(entry_title, entry_info['type'], entry_info['chapsread'], entry_info['readstat'])

# fill up entries list box with all existing entries
def populate_entries():

    # loads existing entries into entries dictionary
    load_entries()

    # iterate through the keys found in entries and list them in the list box
    for entry_title in entries:
        entries_lb.insert('end', entry_title)

# retrieve selected entry selected from entries list box
def get_selected_entry():

    selected_entry = entries_lb.get(entries_lb.curselection())
    return selected_entry

# write the entries dictionary to json save file; entries.save
# def write_entries_to_file():

def del_contents():
    open(storage_filename, 'w').close()

# delete existing entry
def delete_entry():
    
    global entries
    selected_entry = get_selected_entry()
    
    del entries[selected_entry]
    

# customised way of formating json data
def custom_serializer(obj):
    if isinstance(obj, Entry):
        return {
            'title': obj.title, 
            'type': obj.type,
            'chapsread': obj.chapsread, 
            'readstat': obj.readstat
        }
    return obj

# new entry popup function to record entries
def new_entry_popup():

    # new entry function to save new reading entries to json file format
    def new_entry_func():

        # loads existing entries into entries dictionary
        load_entries()

        title = ne_title_entry.get()
        type = ne_type_entry.get()
        chapsread = ne_chapsread_entry.get()
        readstat = ne_readstat_entry.get()

        entries[title] = Entry(title, type, chapsread, readstat)

        json_data = json.dumps(entries, default=custom_serializer, indent=4)

        with open(storage_filename, 'w') as outfile:
            outfile.write(json_data)

        new_entry.destroy()

    new_entry = tk.Toplevel(home_frame, bg='lightyellow')
    new_entry.title('New Entry')
    new_entry.geometry('300x300')
    
    new_entry_title = tk.Label(new_entry, text='Reading Logger | New Entry', bg='lightyellow')
    new_entry_title.grid(row=0, columnspan=2)

    ne_title = tk.Label(new_entry, text='Title:', bg='lightyellow')
    ne_type = tk.Label(new_entry, text='Type:', bg='lightyellow')
    ne_chapsread = tk.Label(new_entry, text='Chapters Read:', bg='lightyellow')
    ne_readstat = tk.Label(new_entry, text='Reading Status:', bg='lightyellow')

    ne_title_entry = tk.Entry(new_entry)
    ne_type_entry = tk.Entry(new_entry)
    ne_chapsread_entry = tk.Entry(new_entry)
    ne_readstat_entry = tk.Entry(new_entry)

    submit_entry = tk.Button(new_entry, text='Add Entry', command=new_entry_func)

    ne_title.grid(row=1, column=0)
    ne_type.grid(row=2, column=0)
    ne_chapsread.grid(row=3, column=0)
    ne_readstat.grid(row=4, column=0)

    ne_title_entry.grid(row=1, column=1)
    ne_type_entry.grid(row=2, column=1)
    ne_chapsread_entry.grid(row=3, column=1)
    ne_readstat_entry.grid(row=4, column=1)

    submit_entry.grid(row=5, columnspan=2)

def update_entry_popup():
    
    # retrieves selected entry's title for dictionary referencing
    entry = get_selected_entry()
    
    update_entry = tk.Toplevel(home_frame, bg='lightgreen')
    update_entry.title('Update Entry')
    update_entry.geometry('300x300')

    update_entry_title = tk.Label(update_entry, text='Reading Logger | Update Entry', bg='lightgreen')
    update_entry_title.grid(row=0, columnspan=2)

    ue_title = tk.Label(update_entry, text='Title:', bg='lightgreen')
    ue_type = tk.Label(update_entry, text='Type:', bg='lightgreen')
    ue_chapsread = tk.Label(update_entry, text='Chapters Read:', bg='lightgreen')
    ue_readstat = tk.Label(update_entry, text='Reading Status:', bg='lightgreen')

    # inserting existing data for selected entry
    ue_title_entry = tk.Entry(update_entry)
    ue_title_entry.insert(0, entries[entry].title)

    ue_type_entry = tk.Entry(update_entry)
    ue_type_entry.insert(0, entries[entry].type)
    
    ue_chapsread_entry = tk.Entry(update_entry)
    ue_chapsread_entry.insert(0, entries[entry].chapsread)
    
    ue_readstat_entry = tk.Entry(update_entry)
    ue_readstat_entry.insert(0, entries[entry].readstat)

    ue_title.grid(row=1, column=0)
    ue_type.grid(row=2, column=0)
    ue_chapsread.grid(row=3, column=0)
    ue_readstat.grid(row=4, column=0)

    ue_title_entry.grid(row=1, column=1)
    ue_type_entry.grid(row=2, column=1)
    ue_chapsread_entry.grid(row=3, column=1)
    ue_readstat_entry.grid(row=4, column=1)

# initial tkinter setup
root = tk.Tk()
root.title('Reading Logger')
root.geometry('300x300')

# home
home_frame = tk.Frame(root, bg='lightblue')
home_frame.pack(expand=True, fill='both')

# center (to be done)
home_title = tk.Label(home_frame, text='Reading Logger | Home', bg='lightblue')
home_title.grid(row=0, columnspan=2)

# left side
entries_lbl = tk.Label(home_frame, text='Entries', bg='lightblue')
entries_lbl.grid(row=1, column=0)

entries_lb = tk.Listbox(home_frame)
entries_lb.grid(row=2, column=0)
populate_entries()

# right side
new_entry_btn = tk.Button(home_frame, text='New Entry', command=new_entry_popup)
new_entry_btn.grid(row=1, column=1, padx=10)

update_entry_btn = tk.Button(home_frame, text='Update Entry', command=update_entry_popup)
update_entry_btn.grid(row=2, column=1, padx=10)

delete_entry_btn = tk.Button(home_frame, text='Delete Entry', command=del_contents)
delete_entry_btn.grid(row=2, column=2, padx=10)

root.mainloop()

# TODO NEXT
# - popup to update existing entries based on selected entry in listbox for entries
# - save new updated entry in lieu of existing entry
# - dynamically update listbox after adding new entry/ updating entry

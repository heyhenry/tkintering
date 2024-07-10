# Resources used: 
# creating listboxes: https://www.geeksforgeeks.org/python-tkinter-listbox-widget/
# centering home title: https://stackoverflow.com/questions/70974175/with-tkinter-grid-method-i-want-to-center-the-labels 
# creating a json file: https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
# creating custom json serializer: https://howtodoinjava.com/python-json/custom-class-serialization/
# closing popup window: https://www.geeksforgeeks.org/how-to-close-a-window-in-tkinter/
# to erase file contents: https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python
# updating json file contents: https://stackoverflow.com/questions/71764921/how-to-delete-an-element-in-a-json-file-python
# opening up web browser: https://stackoverflow.com/questions/31715119/how-can-i-open-a-website-in-my-web-browser-using-python
# aligning label texts: https://stackoverflow.com/questions/31140590/how-to-line-left-justify-label-and-entry-boxes-in-tkinter-grid

import tkinter as tk
import json
import os
import webbrowser

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
storage_filename = 'entries.json'
stats = {'reading': 0, 'read': 0, 'toread': 0}

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
    
    # cleans listbox contents aka erases all items
    entries_lb.delete(0, 'end')

    # iterate through the keys found in entries and list them in the list box
    for entry_title in entries:
        entries_lb.insert('end', entry_title)

# retrieve selected entry selected from entries list box
def get_selected_entry():

    selected_entry = entries_lb.get(entries_lb.curselection())
    return selected_entry

# delete existing entry
def delete_entry():
    
    # retrieve selected entry's key
    selected_entry = get_selected_entry()

    # delete selected entry in save file
    with open(storage_filename, 'r') as file:
        entry_data = json.load(file)
        del entry_data[selected_entry]
    
    # update save file 
    with open(storage_filename, 'w') as file:
        json.dump(entry_data, file, indent=4)
    
    # *** Check if this code is required via test down the line ***
    # deleted entries dictionary alongside file
    del entries[selected_entry]

    # updates reading stats
    updates_stats()

    # updates the display listbox in realtime
    populate_entries()

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

# clear json file contents
def clear_file():

    with open(storage_filename, 'w') as file:
        file.write('{}')

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

        # updates the list of entries showcased in real time
        populate_entries()

        updates_stats()

        new_entry.destroy()

    new_entry = tk.Toplevel(home_frame, bg='lightyellow')
    new_entry.title('New Entry')
    # new_entry.geometry('300x300')
    
    new_entry_title = tk.Label(new_entry, text='Reading Logger | New Entry', bg='lightyellow', font=('Maven Pro Black', 16))
    new_entry_title.grid(row=0, columnspan=2, pady=(0, 10), padx=10)

    ne_title = tk.Label(new_entry, text='Title:', bg='lightyellow', font=('Maven Pro Black', 13))
    ne_type = tk.Label(new_entry, text='Type:', bg='lightyellow', font=('Maven Pro Black', 13))
    ne_chapsread = tk.Label(new_entry, text='Chapters Read:', bg='lightyellow', font=('Maven Pro Black', 13))
    ne_readstat = tk.Label(new_entry, text='Reading Status:', bg='lightyellow', font=('Maven Pro Black', 13))

    ne_title_entry = tk.Entry(new_entry)
    ne_type_entry = tk.Entry(new_entry)
    ne_chapsread_entry = tk.Entry(new_entry)
    ne_readstat_entry = tk.Entry(new_entry)

    submit_entry = tk.Button(new_entry, text='Add Entry', **btn_params, command=new_entry_func)

    ne_title.grid(row=1, column=0, sticky='w', padx=10)
    ne_type.grid(row=2, column=0, sticky='w', padx=10)
    ne_chapsread.grid(row=3, column=0, sticky='w', padx=10)
    ne_readstat.grid(row=4, column=0, sticky='w', padx=10)

    ne_title_entry.grid(row=1, column=1, padx=(0, 10))
    ne_type_entry.grid(row=2, column=1, padx=(0, 10))
    ne_chapsread_entry.grid(row=3, column=1, padx=(0, 10))
    ne_readstat_entry.grid(row=4, column=1, padx=(0, 10))

    submit_entry.grid(row=5, columnspan=2, pady=10)

# updates existing entry
def update_entry_popup():
    
    def update_entry_func(selected_entry):

        # retrieves updated info about selected entry
        title = ue_title_entry.get()
        type = ue_type_entry.get()
        chapsread = ue_chapsread_entry.get()
        readstat = ue_readstat_entry.get()

        # clears whole json file
        clear_file()

        # deletes the currently selected entry
        del entries[selected_entry]

        # creates and adds the new entry aka updated entry
        entries[title] = Entry(title, type, chapsread, readstat)

        # creates the json structure for entries
        json_data = json.dumps(entries, default=custom_serializer, indent=4)

        # writes the json data into the save file aka entries.json
        with open(storage_filename, 'w') as outfile:
            outfile.write(json_data)

        # updates entries list show on home page
        populate_entries()

        # updates reading stats
        updates_stats()

        # closes update entry pop-up
        update_entry.destroy()

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
    ue_title_entry.insert('end', entries[entry].title)

    ue_type_entry = tk.Entry(update_entry)
    ue_type_entry.insert('end', entries[entry].type)
    
    ue_chapsread_entry = tk.Entry(update_entry)
    ue_chapsread_entry.insert('end', entries[entry].chapsread)
    
    ue_readstat_entry = tk.Entry(update_entry)
    ue_readstat_entry.insert('end', entries[entry].readstat)

    ue_update_btn = tk.Button(update_entry, text='Update Entry', command=lambda:update_entry_func(entry))

    ue_title.grid(row=1, column=0)
    ue_type.grid(row=2, column=0)
    ue_chapsread.grid(row=3, column=0)
    ue_readstat.grid(row=4, column=0)

    ue_title_entry.grid(row=1, column=1)
    ue_type_entry.grid(row=2, column=1)
    ue_chapsread_entry.grid(row=3, column=1)
    ue_readstat_entry.grid(row=4, column=1)

    ue_update_btn.grid(row=5, columnspan=2, padx=10, pady=10)

# redirects and opens myanimelist site
def redirect_mal():
    webbrowser.open('https://myanimelist.net/anime.php')

# redirects and opens good reads site
def redirect_goodreads():
    webbrowser.open('https://www.goodreads.com/')

# redirects and opens anilist site
def redirect_anilist():
    webbrowser.open('https://anilist.co/search/anime')

# loads existing reading stats
def load_stats():
    load_entries()
    for entry in entries.keys():
        if entries[entry].readstat == 'reading':
            stats['reading'] += 1
        elif entries[entry].readstat == 'to read':
            stats['toread'] += 1
        elif entries[entry].readstat == 'read':
            stats['read'] += 1

    # updates reading stats display
    stat_reading.set(stats['reading'])
    stat_toread.set(stats['toread'])
    stat_read.set(stats['read'])

# updates reading stats
def updates_stats():

    # cleans stats dictionary
    stats = {'reading': 0, 'read': 0, 'toread': 0}

    # determines key counts for reading status of entries
    for entry in entries.keys():
        if entries[entry].readstat == 'reading':
            stats['reading'] += 1
        elif entries[entry].readstat == 'to read':
            stats['toread'] += 1
        elif entries[entry].readstat == 'read':
            stats['read'] += 1
    
    # updates reading stats display
    stat_reading.set(stats['reading'])
    stat_toread.set(stats['toread'])
    stat_read.set(stats['read'])

# initial tkinter setup
root = tk.Tk()

# initialize reading status variables
stat_reading = tk.StringVar()
stat_toread = tk.StringVar()
stat_read = tk.StringVar()

root.title('Reading Logger')
# root.geometry('300x300')

# load reading stats
load_stats()

# home
home_frame = tk.Frame(root, bg='lightblue')
home_frame.pack(expand=True, fill='both')

# center (to be done)
home_title = tk.Label(home_frame, text='Reading Logger | Home', bg='lightblue', font=('Maven Pro Black', 16))
home_title.grid(row=0, columnspan=2, pady=(10, 0))

# left 
entries_lbl = tk.Label(home_frame, text='Entries', bg='lightblue', font=('Maven Pro Black', 13))
entries_lbl.grid(row=1, column=0, pady=(0, 10))

entries_lb = tk.Listbox(home_frame)
entries_lb.grid(rowspan=3, column=0, padx=15)
         
populate_entries()

btn_params = {'height': 1, 'width': 15, 'font': ('Maven Pro Black', 10)}

# middle
new_entry_btn = tk.Button(home_frame, text='New Entry', **btn_params, command=new_entry_popup)
new_entry_btn.grid(row=2, column=1, padx=10)

update_entry_btn = tk.Button(home_frame, text='Update Entry', **btn_params, command=update_entry_popup)
update_entry_btn.grid(row=3, column=1, padx=10)

delete_entry_btn = tk.Button(home_frame, text='Delete Entry', **btn_params, command=delete_entry)
delete_entry_btn.grid(row=4, column=1, padx=10)

# right
booksreading_lbl = tk.Label(home_frame, text='Books Reading:', bg='lightblue', font=('Maven Pro Black', 11))
booksreading_display = tk.Label(home_frame, textvariable=stat_reading, bg='lightblue', font=('Maven Pro Black', 11))
booksreading_lbl.grid(row=2, column=2, sticky='w')
booksreading_display.grid(row=2, column=3, sticky='e', padx=(0, 10))

booksread_lbl = tk.Label(home_frame, text='Books Read:', bg='lightblue', font=('Maven Pro Black', 11))  
booksread_display = tk.Label(home_frame, textvariable=stat_read, bg='lightblue', font=('Maven Pro Black', 11))
booksread_lbl.grid(row=3, column=2, sticky='w')
booksread_display.grid(row=3, column=3, sticky='e', padx=(0, 10))

bookstoread_lbl = tk.Label(home_frame, text='Books to Read:', bg='lightblue', font=('Maven Pro Black', 11))
bookstoread_display = tk.Label(home_frame, textvariable=stat_toread, bg='lightblue', font=('Maven Pro Black', 11))
bookstoread_lbl.grid(row=4, column=2, sticky='w')
bookstoread_display.grid(row=4, column=3, sticky='e', padx=(0, 10))

# bottom 
recom_one = tk.Button(home_frame, text='MyAnimeList', **btn_params, command=redirect_mal)
recom_two = tk.Button(home_frame, text='Good Reads', **btn_params, command=redirect_goodreads)
recom_three = tk.Button(home_frame, text='AniList', **btn_params, command=redirect_anilist)

recom_one.grid(row=5, column=0, pady=10)
recom_two.grid(row=5, column=1, pady=10)
recom_three.grid(row=5, column=2, pady=10)

root.mainloop()

# TODO NEXT (No Particular Order)

# prioritise: change reading status label font/colours -> change button design to mountainous -> realign existing text

# 1. Continous design/UI improvement
# 1.1 font, redesigning new entry pop-up
# 1.2 font, redesigning update entry pop-up
# 2. Creating a pop-up detailing information about selected entry for viewing only
# 3. Adding a stats section to the home page or separate pop-up
# 4. entry input validations / mitigations
# 4.1 new entry section required
# 4.2 update entry section required

# to think about
# changing new entry to add entry
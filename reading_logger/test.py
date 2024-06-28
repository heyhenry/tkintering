# Resource from Tutorials Point: https://www.tutorialspoint.com/how-do-i-create-a-popup-window-in-tkinter
# Resource from Geeks For Geeks: https://www.geeksforgeeks.org/how-to-close-a-window-in-tkinter/  

import tkinter as tk

# initial tkinter setup
window = tk.Tk()
window.title('Main Window')
window.geometry('300x300')

# function to open pop-up window
def open_popup():
    top = tk.Toplevel(window)
    top.title('Pop-up Window')
    top.geometry('200x200')

    popup_lbl = tk.Label(top, text='Yo! Just popping in!')
    popup_lbl.pack()

    close_popup_btn = tk.Button(top, text='Close Pop-Up', command=top.destroy)
    close_popup_btn.pack()

main_lbl = tk.Label(window, text='Click button for suprise.')
main_lbl.pack()

popup_btn = tk.Button(window, text='Click Me?', command=open_popup)
popup_btn.pack()

window.mainloop()
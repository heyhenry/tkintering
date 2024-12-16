import tkinter as tk
import time

def update_timer():
    timer_val = int(timer_var.get())
    # timer_display.config(text=f'00:00:{timer_val}')
    for i in range(timer_val):
        timer_display.config(text=f'00:00:{i+1}')
        time.sleep(1)

# def update_timer_val(val):
#     timer_display.config(text=f'00:00:{val+1}')

root = tk.Tk()

timer_var = tk.StringVar()

title = tk.Label(root, text='Enter duration of timer (in seconds):', font=('helvetica', 18))
title_entry = tk.Entry(root, textvariable=timer_var, font=('helvetica', 18))
start_timer = tk.Button(root, text='Start Timer', font=('helvetica', 18), command=update_timer)

title.grid(row=0, column=0, pady=20)
title_entry.grid(row=0, column=1, pady=20)
start_timer.grid(row=0, column=2, padx=10, pady=20)

timer_display = tk.Label(root, text='00:00:00', font=('helvetica', 18))
timer_display.grid(row=1, columnspan=3, pady=20)

root.mainloop()

# for reference from a previous project of my own
# # updates the utc time clock (server time)
# def update_utc():
#     # get the current utc time
#     utc_time = dt.datetime.now(timezone.utc)
#     # reformat the time to string
#     string_time = utc_time.strftime('%H:%M:%S')
#     # update the display label to showcase live time
#     utc_livetime_lbl.config(text=f'Server Time: {string_time}')
#     # execute the update_utc function after time elapsed (1 second)
#     utc_livetime_lbl.after(1000, update_utc)


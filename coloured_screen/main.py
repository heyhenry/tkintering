import tkinter as tk

root = tk.Tk()
root.title('Coloured Screen')

btn_params = {'width': 8, 'height': 2}

def bg_colour(colour):
    main_frame.config(bg=colour)
    title_lbl.config(bg=colour)

main_frame = tk.Label(root, bg='white')
main_frame.pack()

title_lbl = tk.Label(main_frame, text="Change Screen Colour", font=('Maven Black Pro', 18))
title_lbl.grid(row=0, columnspan=3)

red_btn = tk.Button(main_frame, text='Red', **btn_params, command=lambda:bg_colour('red'))
green_btn = tk.Button(main_frame, text='Green', **btn_params, command=lambda:bg_colour('green'))
blue_btn = tk.Button(main_frame, text='Blue', **btn_params, command=lambda:bg_colour('blue'))
orange_btn = tk.Button(main_frame, text='Orange', **btn_params, command=lambda:bg_colour('orange'))
purple_btn = tk.Button(main_frame, text='Purple', **btn_params, command=lambda:bg_colour('purple'))
yellow_btn = tk.Button(main_frame, text='Yellow', **btn_params, command=lambda:bg_colour('yellow'))
black_btn = tk.Button(main_frame, text='Black', **btn_params, command=lambda:bg_colour('black'))
pink_btn = tk.Button(main_frame, text='Pink', **btn_params, command=lambda:bg_colour('pink'))
brown_btn = tk.Button(main_frame, text='Salmon', **btn_params, command=lambda:bg_colour('salmon'))

red_btn.grid(row=1, column=0, padx=10, pady=10)
green_btn.grid(row=1, column=1, padx=10, pady=10)
blue_btn.grid(row=1, column=2, padx=10, pady=10)
orange_btn.grid(row=2, column=0, padx=10, pady=10)
purple_btn.grid(row=2, column=1, padx=10, pady=10)
yellow_btn.grid(row=2, column=2, padx=10, pady=10)
black_btn.grid(row=3, column=0, padx=10, pady=10)
pink_btn.grid(row=3, column=1, padx=10, pady=10)
brown_btn.grid(row=3, column=2, padx=10, pady=10)

root.mainloop()

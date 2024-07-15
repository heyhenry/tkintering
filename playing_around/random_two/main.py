import requests
import tkinter as tk

root = tk.Tk()
root.title('URL Shortener')
root.geometry("250x150+800+250")

given_url = tk.StringVar()
result_url = tk.StringVar()

def shorten():
    base_url = 'http://tinyurl.com/api-create.php?url='
    the_url = given_url.get()
    response = requests.get(base_url+the_url)
    short_url = response.text
    result_url.set(short_url)

title_lbl = tk.Label(root, text='Shorten This URL')
url_entry = tk.Entry(root, textvariable=given_url)
shortened_url_entry = tk.Entry(root, textvariable=result_url)
submit_btn = tk.Button(root, text='Shorten URL', command=shorten)

title_lbl.pack(padx=10, pady=5)
url_entry.pack(padx=10, pady=5)
shortened_url_entry.pack(padx=10, pady=5)
submit_btn.pack(padx=10, pady=5)

root.mainloop()
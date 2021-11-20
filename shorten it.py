from tkinter import *
import pyshorteners
import clipboard


window = Tk()

window.geometry("250x200")

window.resizable(False, False)

window.title("Shorten It! by @saarthakofficial")

url_input = Entry(window, font=("Comic Sans", "16"))
url_input.grid(row=1, column=2, pady=6)

str_url = StringVar(window)

shortened_url = Label(window, textvariable=str_url, font=("Arial","16"), fg="#fff", bg="#1abc9c")
shortened_url.grid(row=6, column=2, pady=6)


def copy_short_url():
  try:
    clipboard.copy(str_url.get())
    print("URL Copied Successfully!")
  except:
    str_url.set("Something Went Wrong, Try Again!")


copy_btn = Button(window, text="Copy It!", bg="#34495e", fg="#fff", font=("Arial", "12"), command=copy_short_url)
copy_btn.grid(row=8, column=2, pady=6, padx=10)


def short_url():
  try:
    s = pyshorteners.Shortener()
    url = url_input.get()
    final_result = s.tinyurl.short(url)
    str_url.set(final_result)
    url_input.delete(0, END)
  except:
    str_url.set("Enter URL Please!")


btn = Button(window, text="Shorten It!", padx=8, pady=4, bg="#2ecc71", fg="#fff", font=("Arial","16"), activebackground="#16a085", command=short_url)
btn.grid(row=3, column=2, pady=6)

window.mainloop()
import pyshorteners
import pyperclip
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("URL Shortner")
root.geometry("500x300")
root.configure(bg="white")
root.resizable(0,0)
def short():
    url=pyshorteners.Shortener().tinyurl.short(e.get())
    pyperclip.copy(url)
    messagebox.showinfo("URL Shortner",f"Shortened URL:{url} is copied to clipboard")
Label(root,text="URL Shortner",font="arial 20 bold",bg="white",fg="black").pack(pady=10)
Label(root,text="Enter URL:",font="arial 15 bold",bg="white",fg="black").place(x=10,y=70)
e=Entry(root,width=40,borderwidth=5)
e.place(x=150,y=70)
Button(root,text="Shorten",font="arial 15 bold",bg="white",fg="blue",command=short).place(x=200,y=120)
root.mainloop()

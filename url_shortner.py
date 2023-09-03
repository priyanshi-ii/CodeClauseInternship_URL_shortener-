import tkinter as tk
import pyshorteners
import clipboard
from tkinter import messagebox
root=tk.Tk()
root.title("URL Shortner")
root.geometry("400x200")
root.configure(bg="black")
def short():
    try:
        url=url_entry.get()
        s=pyshorteners.Shortener()
        short_url=s.tinyurl.short(url)
        short_url_entry.insert(0,short_url)
    except:
        messagebox.showerror("Error","Please Enter a valid URL")
def copy():
    url=short_url_entry.get()
    clipboard.copy(url)
    messagebox.showinfo("Success","URL Copied")
url_label=tk.Label(root,text="Enter URL",font=("Arial",15),bg="black",fg="white")
url_label.grid(row=0,column=0,padx=10,pady=10)
url_entry=tk.Entry(root,width=30,font=("Arial",15),bg="black",fg="white")
url_entry.grid(row=0,column=1,padx=10,pady=10)
short_btn=tk.Button(root,text="Short",font=("Arial",15),bg="black",fg="white",command=short)
short_btn.grid(row=1,column=0,padx=10,pady=10)
short_url_entry=tk.Entry(root,width=30,font=("Arial",15),bg="black",fg="white")
short_url_entry.grid(row=1,column=1,padx=10,pady=10)
copy_btn=tk.Button(root,text="Copy",font=("Arial",15),bg="black",fg="white",command=copy)
copy_btn.grid(row=2,column=0,padx=10,pady=10)
root.mainloop()

import tkinter as tk
from tkinter import ttk

def on_scale_change(value):
    label.config(text=f"Value: {value}")

root = tk.Tk()
root.title("Scale Example")
root.geometry("300x100")

scale = tk.Scale(root, from_=0, to=50, resolution=1,
                 orient=tk.VERTICAL, length=200, command=on_scale_change)
scale.set(25)  # Default value when initialized
scale.pack()

label = ttk.Label(root, text="Value: 25")
label.pack()

root.mainloop()

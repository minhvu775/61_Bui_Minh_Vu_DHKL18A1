import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)

def open_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Selected folder:", folder_path)

root = tk.Tk()
root.title('Demo mở file, thư mục.')
root.geometry('300x80')

open_file_button = tk.Button(root, text="Open File", command=open_file)
open_file_button.pack(padx=5, pady=5)

open_folder_button = tk.Button(root, text="Open Folder", command=open_folder)
open_folder_button.pack(padx=5, pady=5)

root.mainloop()

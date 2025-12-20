import tkinter as tk 
from tkinter import ttk 

class ComboboxApp: 
 def __init__(self, root):

    self.root = root 
    self.root.title("Wellcome to Uneti App") 
    self.root.geometry('450x120') 

    self.options=["DHKL16A1", "DHKL 16A2", "DHKL17A1", "DHKL 17A2", "DHKL 17A3", "DHKL 18A1", "DHKL 18A2", "DHKL 18A3"]

    self.teacher_label = tk.Label(root, text="Giảng viên:") 
    self.teacher_label.grid(row=0, column=0, padx=5, pady=5) 

    self.teacher_textbox = tk.Text(root, height=1, width=20) 
    self.teacher_textbox.grid(row=0, column=1, padx=5, pady=5) 

    self.label = tk.Label(root, text="Lớp giảng dạy:") 
    self.label.grid(row=1, column=0, padx=5, pady=5) 

    self.combobox = ttk.Combobox(root, values=self.options) 
    self.combobox.grid(row=1, column=1, padx=5, pady=5) 
    self.combobox.bind("<<ComboboxSelected>>", self.on_select) 

 def on_select(self, event): 
    selected_value = self.combobox.get() 
    print("Selected:", selected_value) 

root = tk.Tk() 
app = ComboboxApp(root) 
root.mainloop()
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Welcome to KHƯD app")
window.geometry('350x200')

def clicked():
    messagebox.askquestion('BM Toán ứng dụng', 'Bạn có muốn nghỉ học không?')

btn = Button(window, text='Bấm vào đây', command=clicked)
btn.grid(column=0, row=0)

window.mainloop()

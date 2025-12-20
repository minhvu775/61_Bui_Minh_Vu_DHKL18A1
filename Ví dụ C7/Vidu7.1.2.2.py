from tkinter import * 

window = Tk() 
window.title("Welcome to Uneti") 
window.geometry('450x120') 
lbl = Label(window, text="Hello") 
lbl.grid(column=0, row=0) 

#Hàm khi nút được nhấn
def clicked(): 
 lbl.configure(text="Button was clicked !!")

#Thêm một nút nhấn Click Me 
btn = Button(window, text="Click Me", bg="yellow", 
 fg="blue",command=clicked) 

#Thiết lập vị trí của nút nhấn có màu nền và màu chữ 
btn.grid(column=5, row=0) 

window.mainloop()
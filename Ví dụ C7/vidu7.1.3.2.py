from tkinter import *

parent = Tk()
parent.geometry("200x100")

# Tạo và định vị nhãn "Name" tại hàng 0, cột 0
name_label = Label(parent, text="Name")
name_label.grid(row=0, column=0)

# Tạo và định vị ô nhập liệu cho tên tại hàng 0, cột 1
e1 = Entry(parent)
e1.grid(row=0, column=1)

# Tạo và định vị nhãn "Password" tại hàng 1, cột 0
password_label = Label(parent, text="Password")
password_label.grid(row=1, column=0)

# Tạo và định vị ô nhập liệu cho mật khẩu tại hàng 1, cột 1
e2 = Entry(parent)
e2.grid(row=1, column=1)

# Tạo và định vị nút "Submit" tại hàng 4, cột 0
submit_button = Button(parent, text="Submit")
submit_button.grid(row=4, column=0)

# Bắt đầu vòng lặp chạy của ứng dụng
parent.mainloop()

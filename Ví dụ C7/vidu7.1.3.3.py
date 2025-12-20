from tkinter import *

# Tạo cửa sổ gốc (root window) và đặt tiêu đề
windows = Tk()
windows.title("Welcome to Uneti!")
windows.geometry("400x150")

# Tạo và đặt nhãn "Name" tại tọa độ tuyệt đối (30, 30)
name_label = Label(windows, text="Name").place(x=30, y=30)

# Tạo và đặt nhãn "Email" tại tọa độ tuyệt đối (30, 60)
email_label = Label(windows, text="Email").place(x=30, y=60)

# Tạo và đặt nhãn "Password" tại tọa độ tuyệt đối (30, 90)
password_label = Label(windows, text="Password").place(x=30, y=90)

# Tạo và đặt ô nhập liệu cho "Name" tại tọa độ tuyệt đối (95, 30)
e1 = Entry(windows).place(x=95, y=30)

# Tạo và đặt ô nhập liệu cho "Email" tại tọa độ tuyệt đối (95, 60)
e2 = Entry(windows).place(x=95, y=60)

# Tạo và đặt ô nhập liệu cho "Password" tại tọa độ tuyệt đối (95, 90)
e3 = Entry(windows).place(x=95, y=90)

windows.mainloop()

from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

# Định nghĩa lớp con có tên là Example, kế thừa từ lớp Frame trong Tkinter.
# Lớp Example đại diện cho ứng dụng.
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Ví dụ sử dụng Frame & Button")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=True)

        # Tạo một Frame với hiệu ứng relief là RAISED (nổi) và borderwidth là 1
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        # Tạo nút Close và đặt vị trí bên phải với giảm độ độ dài và độ cao là 5 pixel
        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)

        # Tạo nút OK và đặt vị trí bên phải
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)

# Tạo cửa sổ gốc (root window) và cấu hình kích thước và vị trí
windows = Tk()
windows.geometry("300x200+300+300")

# Tạo một đối tượng của lớp Example và chạy ứng dụng
app = Example(windows)
windows.mainloop()

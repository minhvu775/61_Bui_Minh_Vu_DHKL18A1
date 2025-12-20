from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Style, Entry

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("Ứng dụng tính toán")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        # Configuring the grid layout
        for i in range(4):
            self.columnconfigure(i, pad=3)
            self.rowconfigure(i, pad=3)

        # Entry widget for display
        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)

        # Buttons for numbers, operators, and functions
        buttons = [
            ("Xóa", 1, 0),
            ("Quay lại", 1, 1),
            ("", 1, 2),
            ("Kết thúc", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("/", 2, 3),
            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("*", 3, 3),
            ("7", 4, 0),
            ("8", 4, 1),
            ("9", 4, 2),
            ("-", 4, 3),
            ("0", 5, 0),
            (".", 5, 1),
            ("=", 5, 2),
            ("+", 5, 3),
        ]

        # Create and place the buttons
        for (text, row, col) in buttons:
            button = Button(self, text=text)
            button.grid(row=row, column=col)

        self.pack()

if __name__ == "__main__":
    windows_root = Tk()
    app = Calculator(windows_root)
    windows_root.mainloop()

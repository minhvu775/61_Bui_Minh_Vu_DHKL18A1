import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Hello World!')

label = QLabel(window)
label.setText('Hello World!')
label.move(50, 50)

window.show()

sys.exit(app.exec_())

import sys
from PySide2.QtWidgets import *
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

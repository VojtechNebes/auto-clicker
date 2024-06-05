import sys
from PyQt5.QtWidgets import QApplication
from ui import CreateUi
from keybind import Keybind

class MyApplication(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.ui = CreateUi(self)
        self.keybind = Keybind(self)

if __name__ == "__main__":
    app = MyApplication()
    sys.exit(app.exec_())
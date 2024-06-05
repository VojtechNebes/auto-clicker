from clicker import Clicker
from pynput.mouse import Button
from pynput.keyboard import Listener, KeyCode, Key

class Keybind():
    def __init__(self, app):
        print("Keybind.__init__()")
        self.ui = app.ui
        self.changingKeybind = False
        
        self.changeKeybind(KeyCode.from_char("e"))
        
        self.ui.keybindChangeBtn.clicked.connect(self.onKeybindChangeBtnClicked)

        listener = Listener(on_press=self.onKeyPress)
        listener.start()

    def onKeyPress(self, key):
        if self.changingKeybind:
            self.changingKeybind = False
            self.changeKeybind(key)
        else:
            if key == self.keybind:
                try:
                    self.clicker.stop()
                except:
                    self.clicker = Clicker(self.ui)
                    self.clicker.start()

    def onKeybindChangeBtnClicked(self):
        self.ui.keybindChangeBtn.setText("...")
        self.changingKeybind = True

    def changeKeybind(self, key):
        self.keybind = key
        self.updateKeybindChangeBtnText()

    def updateKeybindChangeBtnText(self):
        try:
            self.ui.keybindChangeBtn.setText(self.keybind.name)
        except:
            self.ui.keybindChangeBtn.setText(str(self.keybind)[1].upper())
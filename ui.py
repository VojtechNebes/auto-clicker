import PyQt5
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QDoubleSpinBox, QComboBox
from PyQt5.QtGui import QFont
from pynput.mouse import Button

FONT = QFont("MS Shell Dlg 2", 9)

class CreateUi(QWidget):
    def __init__(self, app):
        super().__init__()
        
        self.setFixedSize(308, 129)
        self.setWindowTitle("Auto Clicker")
        
        self.label = QLabel(self)
        self.label.setGeometry(14, 6, 200, 28)
        self.label.setFont(FONT)
        self.label.setText("Start/stop keybind:")
        
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(14, 41, 200, 22)
        self.label_2.setFont(FONT)
        self.label_2.setText("Delay:")
        
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(14, 70, 200, 22)
        self.label_3.setFont(FONT)
        self.label_3.setText("Max. random delay:")
        
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(14, 99, 200, 22)
        self.label_4.setFont(FONT)
        self.label_4.setText("Button:")
        
        self.keybindChangeBtn = QPushButton(self)
        self.keybindChangeBtn.setGeometry(213, 7, 83, 28)
        self.keybindChangeBtn.setFont(FONT)
        
        self.delaySpinBox = QDoubleSpinBox(self)
        self.delaySpinBox.setGeometry(213, 41, 81, 22)
        self.delaySpinBox.setFont(FONT)
        self.delaySpinBox.setDecimals(2)
        self.delaySpinBox.setMaximum(999)
        self.delaySpinBox.setSingleStep(0.01)
        self.delaySpinBox.setSuffix("s")
        self.delaySpinBox.setValue(0.01)
        
        self.delayRandomSpinBox = QDoubleSpinBox(self)
        self.delayRandomSpinBox.setGeometry(213, 70, 81, 22)
        self.delayRandomSpinBox.setFont(FONT)
        self.delayRandomSpinBox.setDecimals(2)
        self.delayRandomSpinBox.setMaximum(2)
        self.delayRandomSpinBox.setSingleStep(0.01)
        self.delayRandomSpinBox.setSuffix("s")
        self.delayRandomSpinBox.setValue(0)
        
        self.buttonComboBox = QComboBox(self)
        self.buttonComboBox.setGeometry(213, 99, 81, 22)
        self.buttonComboBox.setFont(FONT)

        self.buttonComboBox.addItem("Left", Button.left)
        self.buttonComboBox.addItem("Middle", Button.middle)
        self.buttonComboBox.addItem("Right", Button.right)

        self.show()
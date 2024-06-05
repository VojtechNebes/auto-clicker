import time
import threading
import random
from pynput.mouse import Button, Controller

class Clicker(threading.Thread):
    def __init__(self, ui):
        super().__init__()
        
        self.delay = ui.delaySpinBox.value()
        self.delayRandom = ui.delayRandomSpinBox.value()
        self.button = ui.buttonComboBox.currentData()
        self.delayRandom_decimals = ui.delayRandomSpinBox.decimals()
        
        self.running = True
        
        self.mouse = Controller()

    def run(self):
        while self.running == True:
            self.mouse.click(self.button)
            
            try:
                totalDelay = self.delay + random.randrange(0, self.delayRandom * 10**(self.delayRandom_decimals+1)) / 10**(self.delayRandom_decimals+1)
            except:
                totalDelay = self.delay
            
            time.sleep(totalDelay)

    def stop(self):
        if self.running:
            self.running = False
        else:
            raise Exception("not running")
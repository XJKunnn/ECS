import RPi.GPIO as gpio
from time import sleep
import time
import threading

class checkThread(threading.Thread):
    def __init__(self, threadID, name, door):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.door = door
        if(door == 17):
            self.nu = 1
        else:
            self.nu = 2
        
    def run(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self.door, gpio.IN)
        
        if(self.nu == 2):
            sleep(0.1)
        
        while True:
            sleep(0.5)
            if(gpio.input(self.door)):
                print(time.strftime('%Y/%m/%d/%H:%M:%S', time.localtime(time.time())) +" door", self.nu , " alarm")
            else:
                print( self.nu , " safe ")
        gpio.cleanup(self.door)
        
gpio.setmode(gpio.BCM)

gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.output(18, gpio.LOW)
gpio.output(23, gpio.LOW)
check1 = checkThread(1, "checkdoor1", 17)
check2 = checkThread(2, "checkdoor2", 22)
check1.start()
check2.start()
for i in range(1, 10):
    if(i == 5):
        gpio.output(18, gpio.HIGH)  # someone crash into door1
    else: 
        gpio.output(18, gpio.LOW)
    if(i == 8):
        gpio.output(23, gpio.HIGH)  #someone crash into door2
    else:
        gpio.output(23, gpio.LOW)
    sleep(1)

gpio.cleanup(18)
gpio.cleanup(23)


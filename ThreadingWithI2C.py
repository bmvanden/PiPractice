"""
Threading example from: https://www.tutorialspoint.com/python/python_multithreading.htm
"""


#!/usr/bin/python
import tkinter as tk
import threading
import time
import smbus2
bus = smbus2.SMBus(1)

exitFlag = 0

class I2CThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        ATMegaData = [0, 1, 3, 50] #, 80, 0, 0, 0])
        PiData = [3, 10, 120]

        time.sleep(2)

        while (1):
            """
            Read 7 bytes from ATMega (2 bytes FuelCellCurrent, 2 bytes 
            FuelCellVoltage, 2 bytes BatteryVoltage, 1 byte ATMega status)

            Address:    8
            Offset:     0
            of Bytes:   7
            """
            with smbus2.SMBusWrapper(1) as bus:
                ATMegaData = bus.read_i2c_block_data(8, 0, 4)

        #   data = bus.read_byte_data(8, 0)

        #   block = bus.read_i2c_block_data(8, 0, 4)
        #   block2 = struct.unpack("<HHHH",block)
        #   print(data)
        #   print('\n')

        #   for received in block:
        #       ATMegaData[1] = received

        #   ATMegaData = struct.unpack('l', ''.join([chr(i) for i in block[:4]))[0]
        #   ATMegaData[0] = bus.read_byte(8)
        #   ATMegaData[1] = bus.read_byte(8,1)


            time.sleep(0.5)

            """
            Write 3 bytes to ATMega (1 byte FanSpeed, 1 byte Target Current,
            1 byte Pi Status)

            Address:    8
            Offset:     0
            # of bytes: 3
            """
            with smbus2.SMBusWrapper(1) as bus:
                bus.write_i2c_block_data(8, 42, [43,23])

        #   value = 3
        #   bus.write_word_data(8, 0, value)

            time.sleep(0.5)

            print("ATMega Data: ")
            for i in ATMegaData:
                print(i)
            print(ATMegaData)

            print("\nPi Data: ")
            for i in PiData:
                print(i)

class GUIThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        # Create the main window
        root = tk.Tk()
        root.title("EcoCar GUI")         
        # Set window size to match 7" SparkFun LCD (800 x 480)
        root.resizable(False, False)
        root.geometry("800x480")

        #Display Variable Values for Pi and ATMega
        PiDataLabel1 = tk.label(root, text=PiData[0])
        PiDataLabel1.pack()

        # Run forever!        
        root.mainloop()

def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = I2CThread(1, "Thread-1", 1)
thread2 = GUIThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")
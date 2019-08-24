"""
Threading example from: https://www.tutorialspoint.com/python/python_multithreading.htm
"""


#!/usr/bin/python
import tkinter as tk
import threading
import time
import I2CThread

exitFlag = 0

# Holds data to be received from ATMega
ATMegaData = [0, 1, 3, 50, 80, 0, 0, 5]

# Holds data to be sent to ATMega
PiData = [3, 10, 120]




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

        #Data for live update of GUI
        # PiData0 = tk.IntVar()
        # PiData1 = tk.IntVar()
        # PiData2 = tk.IntVar()
        # PiData0.set(PiData[0])
        # PiData1.set(PiData[1])
        # PiData2.set(PiData[2])

        #Display Variable Values for Pi and ATMega
        # PiDataTitle = tk.Label(root, text="Pi Data")
        # PiDataTitle.pack()

        # PiDataLabel1 = tk.Label(root, textvariable=PiData0)
        # PiDataLabel1.pack()
        # PiDataLabel2 = tk.Label(root, textvariable=PiData1)
        # PiDataLabel2.pack()
        # PiDataLabel3 = tk.Label(root, textvariable=PiData2)
        # PiDataLabel3.pack()
        # PiDataUpdateButton = tk.Button(root, text="Increment Values", command=incrementValues)
        # PiDataUpdateButton.pack()

        # Run forever!        
        root.mainloop()

#def incrementValues():
    # PiData[0] = PiData[0] + 1
    # PiData[1] = PiData[1] + 1
    # PiData[2] = PiData[2] + 1
    # PiData0.set(PiData[0])
    # PiData1.set(PiData[1])
    # PiData2.set(PiData[2])

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

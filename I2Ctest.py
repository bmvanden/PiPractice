"""
I2Ctest.py

Tests I2C communication between Pi and ATMega
"""

from smbus2 import SMBusWrapper
import tkinter as tk
import threading as thread
import time

ATMEGA_ADDRESS = 8

ATMegaData = [0, 1, 3, 50, 80, 0, 0, 0]
PiData = [3, 10, 120]

def initI2C():
    while (1):
        """
        Read 7 bytes from ATMega (2 bytes Fu elCellCurrent, 2 bytes 
        FuelCellVoltage, 2 bytes BatteryVoltage, 1 byte ATMega status)

        Offset:     0
        # of Bytes: 7
        """
        with SMBusWrapper(1) as bus:
            ATMegaData = bus.read_i2c_block_data(ATMEGA_ADDRESS, 0, 7)

        time.sleep(0.5)
        
        print("ATMega Data: ")
        for i in ATMegaData:
            print(i)

        """
        Write 3 bytes to ATMega (1 byte FanSpeed, 1 byte Target Current,
        1 byte Pi Status)

        Offset:     0
        # of bytes: 3
        """
        with SMBusWrapper(1) as bus:
            bus.write_i2c_block_data(ATMEGA_ADDRESS, 0, PiData)

        time.sleep(0.5)

        print("\nPi Data: ")
        for i in PiData:
            print(i)

def initGUI():
    # Create the main window
    root = tk.Tk()
    root.title("EcoCar GUI")
    
    # Set window size to match 7" SparkFun LCD (800 x 480)
    root.resizable(False, False)
    root.geometry("800x480")

    # Run forever!
    root.mainloop()


# Create a thread for each function to allow them to run simultaneously
try:
    thread.start_new_thread(initI2C)
    thread.start_new_thread(initGUI)
except:
    print("Error: unable to start threads")

while (1):
    pass

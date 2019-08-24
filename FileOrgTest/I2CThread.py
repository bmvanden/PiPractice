import threading
import time
import smbus2

# Holds data to be received from ATMega
ATMegaData = [0, 1, 3, 50, 80, 0, 0, 5]

# Holds data to be sent to ATMega
PiData = [3, 10, 120]

class I2CThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)

        # Give threads time to initialize
        time.sleep(2)

        while (1):
            """
            Read 7 bytes from ATMega (2 bytes FuelCellCurrent, 2 bytes 
            FuelCellVoltage, 2 bytes BatteryVoltage, 1 byte ATMega status)

            Address:    8
            Offset:     0
            of Bytes:   7
            """
            try:
                with smbus2.SMBusWrapper(1) as bus:
                    ATMegaData = bus.read_i2c_block_data(8, 0, 8)
            except:
                print("Read Error")
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
            try:
                with smbus2.SMBusWrapper(1) as bus:
                    bus.write_i2c_block_data(8, 42, [PiData[0],PiData[1],PiData[2]])
                PiData[0] += 1
                PiData[1] += 2
                PiData[2] -= 1
            except:
                print("Write Error")
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
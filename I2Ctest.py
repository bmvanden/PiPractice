"""
I2Ctest.py

Tests I2C communication between Pi and ATMega
"""

from smbus2 import SMBusWrapper
import time

ATMegaData = [0, 1, 3, 50, 80, 0, 0, 0]
PiData = [3, 10, 120]

while (1):
	"""
	Read 7 bytes from ATMega (2 bytes FuelCellCurrent, 2 bytes 
	FuelCellVoltage, 2 bytes BatteryVoltage, 1 byte ATMega status)

	Address: 	8
	Offset:  	0
	# of Bytes:	7
	"""
	with SMBusWrapper(1) as bus:
		ATMegaData = bus.read_i2c_block_data(8, 0, 7)

	time.sleep(0.5)

	"""
	Write 3 bytes to ATMega (1 byte FanSpeed, 1 byte Target Current,
	1 byte Pi Status)

	Address:	8
	Offset:		0
	# of bytes: 3
	"""
	with SMBusWrapper(1) as bus:
		bus.write_i2c_block_data(8, 0, PiData)

	time.sleep(0.5)

	print("ATMega Data: ")
	for i in ATMegaData:
		print(i)

	print("\nPi Data: ")
	for i in PiData:
		print(i)

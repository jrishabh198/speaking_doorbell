import serial
ser = serial.Serial(
    port='COM5',
    baudrate=15200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
while(1):
	print(ser.read(1))
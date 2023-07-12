import serial


while(True):
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=57600)
    ser.close
    ser.open
    data = ser.readline()
    print(data)
    ser.close
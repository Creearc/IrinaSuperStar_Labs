import serial

ser = serial.Serial('COM6', 9600, timeout=0,
                    parity=serial.PARITY_EVEN, rtscts=1)
while True:
    s = ser.read()
    if s != b'':
        print(s)
    if s == b'1':
        ser.write(b'0')

ser.close() 

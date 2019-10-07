import serial

ser = serial.Serial('COM8', 9600, timeout=0)
while True:
    s = ser.read(10)
    if s != b'':
        s = str(s, 'utf-8').split('/')
        print(s)
        if len(s) < 2:
            continue
        rx = s[0]
        ry = s[1][:-2]
        print(rx, ry)

ser.close() 

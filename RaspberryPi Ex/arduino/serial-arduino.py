import serial 
s = serial.Serial('/dev/ttyACM0', 9600) 
data = raw_input('Send to Arduino: ') 
s.write(data) 
print(s.readline()) 
s.close()

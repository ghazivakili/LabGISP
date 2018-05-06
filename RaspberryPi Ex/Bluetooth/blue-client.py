import bluetooth as bt 
sock = bt.BluetoothSocket(bt.RFCOMM) 
sock.connect(('08:D4:0C:97:CD:6C', 1)) 
data = raw_input('Send via Bluetooth: ') 
sock.send(data) 
print(sock.recv(512)) 
sock.close()

import bluetooth as bt 
sock = bt.BluetoothSocket(bt.RFCOMM) 
sock.bind(('', 1)) 
sock.listen(1) 
client_sock, client_addr = sock.accept() 
print('Connected to', client_addr) 
data = client_sock.recv(512) 
client_sock.send(data) 
client_sock.close() 
sock.close()

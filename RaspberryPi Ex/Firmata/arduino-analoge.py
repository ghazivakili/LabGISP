import pyfirmata 
import time 
#board = pyfirmata.Arduino('/dev/ttyACM0')
board = pyfirmata.util.get_the_board(base_dir='/dev/serial/by-id/', identifier='usb-') 
it = pyfirmata.util.Iterator(board) 
it.start() 
A0=board.get_pin('a:0:i')
A1=board.get_pin('a:1:i')
A2=board.get_pin('a:2:i')
A3=board.get_pin('a:3:i')
time.sleep(1)

while True: 
	print(A0.read()*5.000 , A1.read()*5.000,A2.read()*5.000,A3.read()*5.000)
	#print(A0.read() , A1.read(),A2.read(),A3.read())
	time.sleep(1)


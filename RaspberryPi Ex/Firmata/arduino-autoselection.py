import pyfirmata 
import time 
board =board = pyfirmata.util.get_the_board(base_dir='/dev/serial/by-id/', identifier='usb-') 
pin13 = board.get_pin('d:13:o') 
while True:
    time.sleep(1)
    print("on")
    pin13.write(1)
    time.sleep(1)
    print("off")
    pin13.write(0)

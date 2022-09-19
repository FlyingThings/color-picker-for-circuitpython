import usb_cdc
import time
import neopixel
import board

#Turn off the neopixel on the board
boardpix = neopixel.NeoPixel(board.NEOPIXEL,1, brightness = .1)
boardpix[0] = [0,0,0]

#Check if comport connnected
if usb_cdc.data.connected:
    print('connected')

while True:
    byte_stream = usb_cdc.data.readline()
    #decode from bytes to string, strip whitespace '\n', split values by ','
    split_list = byte_stream.decode('ASCII').strip().split(',')
    #converts list of strings to ints
    data_list = [eval(i) for i in split_list]
    
    #check if the data_list is like [0,0,0,0.0]
    if len(data_list) == 4:
        boardpix.brightness = data_list[3]
    else:
        boardpix[0] = data_list
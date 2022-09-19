from tkinter import *
from tkinter import colorchooser
import serial
#adafruit example: searching for a circuitpython dataport
import adafruit_board_toolkit.circuitpython_serial

comports = adafruit_board_toolkit.circuitpython_serial.data_comports()
if not comports:
    raise Exception("No CircuitPython boards found")

# Print the device paths or names that connect to a REPL.
print([comport.device for comport in comports])

#connects to the found dataport
#if not searching automatically, change comports[0].device to 'COM9' or your comport
port = serial.Serial(
    port = comports[0].device,
    baudrate=115200,
    bytesize = 8,
    timeout=2,
    stopbits=1
    )

#create root window
gray = '#454545'
root =  Tk()
root.title('picker')
root.geometry('350x300')
root.configure(bg=gray)
#slider variables
Rcurrent_value = IntVar()
Gcurrent_value = IntVar()
Bcurrent_value = IntVar()
brightness_value = DoubleVar()
slider_length = 300

#slider event, slider change. Acts on sliding the slider
#Changes the label and writes values to the comport
def slider_changed(event):
    RBG_label.configure(text=str([Rcurrent_value.get(),Gcurrent_value.get(),Bcurrent_value.get()]))
    port.write(b'%d,%d,%d\n'%(Rcurrent_value.get(),Gcurrent_value.get(),Bcurrent_value.get()))
    color_preview.configure(bg = '#%02x%02x%02x'%(Rcurrent_value.get(),Gcurrent_value.get(),Bcurrent_value.get()))
    #print('#%02x%02x%02x'%(Rcurrent_value.get(),Gcurrent_value.get(),Bcurrent_value.get()))

#Brightness slider change event sents an additional value in the list, making it different from the other events
def brightness_change(event):
	RBG_label.configure(text=str([Rcurrent_value.get(),Gcurrent_value.get(),Bcurrent_value.get(),brightness_value.get()]))
	port.write(b'%d,%d,%d,%.2f\n'%(Rcurrent_value.get(),Gcurrent_value.get(),Bcurrent_value.get(),brightness_value.get()))

#Slider setups
Rslider = Scale(
    root,
    from_=0,
    to=255,
    orient='horizontal',
    variable=Rcurrent_value,
    command=slider_changed,
    length = slider_length,
    label = 'Red',
    bg = gray,
    fg = '#FFF'
    )
Gslider = Scale(
    root,
    from_=0,
    to=255,
    orient='horizontal',
    variable=Gcurrent_value,
    command=slider_changed,
    length = slider_length,
    label = 'Green',
    bg = gray,
    fg = '#FFF'
    )
Bslider = Scale(
    root,
    from_=0,
    to=255,
    orient='horizontal',
    variable=Bcurrent_value,
    command=slider_changed,
    length = slider_length,
    label = 'Blue',
    bg = gray,
    fg = '#FFF'
    )
brightness_slider = Scale(
	root,
    from_=0,
    to=1,
    orient='horizontal',
    variable=brightness_value,
    command=brightness_change,
    length = slider_length,
    label = 'Brightness',
    bg = gray,
    fg = '#FFF',
    resolution = 0.01 #Steps of 0.01
    )
Rslider.grid(
column=1,
row=0
)
Gslider.grid(
column=1,
row=1
)
Bslider.grid(
column=1,
row=2
)
brightness_slider.grid(
	column=1,
	row = 3)
RBG_label = Label(
    root,
    text = str([Rcurrent_value.get(),Gcurrent_value.get(),Bcurrent_value.get(),brightness_value.get()]),
    bg = gray,
    fg = '#FFF'
    )
RBG_label.grid(
    column=1,
    row=4
    )
color_preview = Canvas(
	height = 30,
	width = 300,
	bg = '#000000'
	)
color_preview.grid(
	column=1,
	row = 5
	)
root.mainloop()


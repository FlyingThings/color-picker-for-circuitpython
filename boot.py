#This enables the data port, seperate from REPL
#REPL(console) is enabled by default
import usb_cdc

usb_cdc.enable(data=True)
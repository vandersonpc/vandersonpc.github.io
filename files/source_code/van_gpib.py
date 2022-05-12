####
#
# Simple GPIB communication program v0.1 (python 3.0)
#
# 2022 - By Vanderson Carvalho - vandersonpc.at.gmail.com
#
####
#####

# import python libraries

import serial
from time import sleep
from statistics import mean

# configure serial port
serial_port = "/dev/tty.usbserial-FTFBXWN5" # system serial port

# serial port initiation
ser = serial.Serial(port = serial_port, baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

# Wait 1 seconds
sleep(1)

##
# snd_read_cmd(): send command to instrument
#

def snd_read_cmd():
    # clearing Output Buffer
    ser.flushOutput()
    # send Command
    ser.write(b"*IDN?\r\n")

#### end of functions ####

# send command to the instrument
snd_read_cmd()

# reading all bytes available bytes till EOL
line = ser.readline()
if line: # there's data?
    # wait 0.1s - serial comms stabilize
    sleep(0.1)
    # decode and print response from the instrument
    print("\n")
    print(line.decode())
# close serial port
ser.close()

####
# van_gpib_gph.py
#
# Plot measure value from serial port v0.1 (python 3.0)
#
# 2022 - By Vanderson Carvalho - vandersonpc.at.gmail.com
#
####
#####

# import python libraries
import serial
import time
import csv
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np

# configure serial port
serial_port = "/dev/tty.usbserial-FTFBXWN5" # system serial port

# serial port initiation
ser = serial.Serial(port = serial_port, baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

ser.flushInput() # clear all serial data

##
# snd_read_cmd(): send command to instrument
#

def snd_read_cmd():
    # Clearing Output Buffer
    ser.flushOutput()
    # Send Command
    ser.write(b"READ?\r\n")

#### end of functions ####

plot_window = 20   # plot window size
y_var = np.array(np.zeros([plot_window])) # create value array

# start plotting
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(y_var)

while True:
    try:
        # Send read commend
        snd_read_cmd()
        ser_bytes = ser.readline()
        try:
            decoded_bytes = float(ser_bytes[0:len(ser_bytes)-7].decode("utf-8"))
            print(decoded_bytes)
        except:
            continue
        with open("test_data.csv","a") as f: # save data into a CSV file
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(),decoded_bytes])
        y_var = np.append(y_var,decoded_bytes)
        y_var = y_var[1:plot_window+1]
        line.set_ydata(y_var)   # plot data
        ax.relim()
        ax.autoscale_view()     # auto scale
        fig.canvas.draw()
        fig.canvas.flush_events()
    except:
        print("Keyboard Interrupt")
        break

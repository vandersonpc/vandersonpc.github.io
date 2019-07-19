---
layout: post
title:  "Reprogramming cheeper USBee AX Pro Logic Analyser "
date:   2019-07-19 10:47:05 -0300
author: Vanderson Pimenta
categories: USB, Electronic, Guides
---

It’s a guide to reprogram your cheap USBee device to use it with the Saleae Software Logic, the USB VID/PID need to be changed. The guide is for LINUX OS only.

(img)(img)

### To achieve that , some tools need to be installed as below:

```
$ sudo aptitude install fxload
$ sudo aptitude install libusb-1.0-0-dev
$ git clone https://github.com/ribalda/fx2eeprom.git
$ cd fx2eeprom
$ make
```
 
### Identify the USB bus and device numbers

```
$ lsusb
...
Bus 001 Device 017: ID 08a9:0014 CWAV Inc. USBee AX-Pro
...
```
### Flash the device
```
sudo fxload -D /dev/bus/usb/001/017 -t fx2lp -I vend_ax.hex
```
### Read and save the first 8 bytes from the device eeprom to a file
```
sudo ./fx2eeprom r 0x08a9 0x0014 8 > eeprom.dat
```
### Edit the VID/PID from the dump file with your favorite hex editor

* Before edition 
```
$ hexdump -C eeprom.dat.bak 
00000000  c0 a9 08 14 00 00 1b 00                        |........|
00000008
```
* After edition
```
$ hexdump -C eeprom.dat
00000000  c0 25 09 81 38 00 1b 00                        |.%..8...|
00000008
```
### Write the new values to device eeprom
```
$ cat eeprom.dat | sudo ./fx2eeprom w 0x08a9 0x0014 8
```
### Unplug & plug you USBee device 
```
$ lsusb
...
Bus 001 Device 019: ID 0925:3881 Lakeview Research Saleae Logic
...
```
Now enjoy your new logic analyser!

Remember, it’s a cheap device. Don’t expected to have a perfect sampling above 1MHz. It’s good for PIC, Arduino and not critical device work.

See you soon! Peace!!!🖖🏻

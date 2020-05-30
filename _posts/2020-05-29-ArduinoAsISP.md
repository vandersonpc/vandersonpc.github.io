---
layout: post
title: "Use Arduino as ISP on MacOs"
date: 2020-05-29
author: Vanderson Pimenta
tags:
  - Electronic, Arduino
---

This article shows how to use the Arduino Pro Mini as a ISP (In-Circuit Serial Programmer) for AVR microcontrollers or another Arduino board.

1. Install brew installer

	```bash
	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
	```
	
	PS: _If the screen prompts you to enter a password, please enter your Mac's user password to continue. When you type the password, it won't be displayed on screen, but the system would accept it. So just type your password and press ENTER/RETURN key. Then wait for the command to finish. _
	
2. Install the avrdude
	```bash
	brew install avrdude
	```
	
	avrdude is the software used to communicate with the Arduino and upload the software to the slave microcontroller_ 

3. Load the ArduinoISP sketch

	ArduinoISP Sketch can be found on the Arduino Editor examples

4. Uncomment the line:
 
	```c
	define USE_OLD_STYLE_WIRING

	```
5. Change the BAUD RATE to 38400
	That was the fastest speed the worked for me.
	
	```c
	define BAUDRATE 38400 
	```
6. Compile and Upload the Sketch

7. Connect the PROGRAMMER and the TARGET as the picture below:
 
	![](https://www.arduino.cc/en/uploads/Tutorial/Arduino_ISP_wires.jpg)
8. Execute avrdude

	```bash
	avrdude -p m328p -P /dev/cu.SLAB_USBtoUART -c avrisp  -V -b 38400 -U flash:w:TransistorTester.hex -U eeprom:w:TransistorTester.eep 
	```
PS: replace the ```/dev/cu.SLAB_USBtoUART```option by the serial port to be used.

The avrdude software documentation can be downloaded [Here](http://download.savannah.gnu.org/releases/avrdude/)

More information to how to use an Arduino as ISP can be found [Here](https://www.arduino.cc/en/Tutorial/ArduinoISP)
---
layout: post
title: Arduino/ATMEL AVR ISP Using Pro Mini
date: 2020-05-30
author: Vanderson Carvalho
categories: [Electronic, Projects, Microcontrollers, Tools]
tags: [arduino, programmer]
image: images/arduino_isp_fp.png
---
This project shows how to use an Arduino Pro Mini as ISP (In Circuit Serial Programmer) device. This ISP can be used to programming Arduino boards as well ATMEL/Microchip AVR microcontrollers. 

Below is the ISP stripboard assembled with all components and the connectors and jumpers pinout. The board was created using the [DIYLC Software](https://github.com/bancika/diy-layout-creator/releases).

![]({{ site.url }}{% link images/arduino_isp_brd.png %})

The picture below shown the real board assembled.

![]({{ site.url }}{% link images/arduino_isp_img.jpg %})


The LEDs can give visual feedback about the device programming process as below:

Color | Function
--- | ---
Red | - Error occurs during the device programming
Green | - Heart Beat. Indicates ISP hardware is running
Blue | - ISP is programming the target device  

>

The jumpers give the options to select the baudrate (19200 or 38400) and if the target device will be powered by the ISP hardware. 

A serial to USB converter device is required in order to connect the ISP Hardware (Arduino Pro Mini) to computer. 

Below is the device connected to an Arduino Leonardo board and a Serial to USB converter.

![]({{ site.url }}{% link images/arduino_isp_img1.jpg %})


The source code for this project and the DIYLC board files can be found [HERE](https://github.com/vandersonpc/MyArduinoISP) on my Github page.

This programmer can be used with the AVRDUDE software described on [this post]({{ site.url }}{% link _posts/2020-05-29-ArduinoAsISP.md %})

Enjoy it! 🖖 

Vanderson 🤓

### License 
>

>All projects are supplied "AS IS" for individual use only. Commercial use is not authorised.  

 
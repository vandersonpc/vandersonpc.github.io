---
layout: post
title:  PIC clock source
date:   2022-05-07 00:00:00 -0300
author: Vanderson Carvalho
categories: [Electronic, Repair, Test Equipment, Tools, Python, TTI1906]
tags: [multimeter, repair, test equipment, python, tti1906]
image: images/ebay_multimeter_fp.png
show_image: false
comments: True
published: false
---

Clock sources are very useful piece of kit, specially when we want to work with digital or microcontroller circuits.

At design or debug phase we may do not need a hundreds of Megahertz clock, rather we need a reliable and flexible clock source, that can be put on hold or can run on step-by-step way.

The propose clock source circuit is based on a PIC 18Fxxxx microcontroller, and has the following characteristics:

* Clock frequency: 1 Hz to 100 KHz
* Operation modes: Free run / Hold (step-by-step)
*

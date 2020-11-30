# Raspberry Pi Robot
The objective of this project is to learn how to make a robot that will react to things around it and to keep a specific distance from them.  First and foremost, it is a learning experience.  There are other projects out there that do the same basic thing.  It is very easy to copy others work, but little to nothing will be learned from just cloning a project.

This project starts with a blank sheet of paper and a few ideas on how to get started.  It is open ended because the project is for fun and learning.


## Student Activities
* Wheel size calculations:  <https://docs.google.com/document/d/1r26n8juQ5lPLR1QN9rYWPgbAS4wTSarJeQLGqS7e-RY/edit?usp=sharing/>
* Torque calculations:  To do item
* Gear ration calculations:  To do item

## To Do List (not in any order)
* Design robot body
* Design robot wheels
* Figure out stepper motor drive to wheels

## Parts list

All parts are available on Amazon or other on-line sources.  This is only a starting point.  You may wish to add items such as LED's, different sensors,  more distance sensors, etc.

*  Raspberry Pi 3, 4 or Zero W  (Zero W prefered)
*  10 Ah (minimum) USB power supply
*  (2) HC-SR04 ultrasonic sensor
*  (2) ROHS Stepper motor 28BYJ-48
*  (2) ULN2003 Stepper motor driver
*  470 ohm resistors
*  330 ohm resistors
*  Bread board
*  Dupont jumper wires 

## Raspberry Pi connections

Pin out:

| Physical pin | BCM/GPIO | Connected to                    |
|--------------|----------|---------------------------------|
| 12           | GPIO18   | Status LED                      |
| 14           |          | Status LED GND                  |
| 32           | GPIO12   | Stepper Coil A-1                |
| 33           | GPIO13   | Sonic distance echo             |
| 36           | GPIO16   | Stepper Coil A-2                |
| 37           | GPIO26   | Sonic distance trigger          |
| 38           | GPIO20   | Stepper Coil B-1                |
| 40           | GPIO21   | Stepper Coil B-2                |

Note: Power for the stepper motor come from an external source due to power limits of the Raspberry Pi.

Pinout of Raspberry PI GPIO:
<https://www.raspberrypi.org/documentation/usage/gpio/>



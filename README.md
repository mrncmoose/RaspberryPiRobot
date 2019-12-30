# Raspberry Pi Robot
The objective of this project is to learn how to make a robot that will react to things around it and to keep a specific distance from them.  First and foremost, it is a learning experience.  There are other projects out there that do the same basic thing.  Very easy to copy, but little to nothing will be learned from just cloning a project.

This project starts with a blank sheet of paper and a few ideas on how to get started.  It is open ended because the project is for fun and learning.

Current work is to create base classes that will handle distance functions, movement functions and rules for when to move and how much based on distance sensed.

## To Do List (not in any order)
* Design robot body
* Design robot wheels
* Figure out stepper motor drive to wheels

## Parts list
*  Raspberry Pi 3, 4 or Zero W
*  5V power supply
*  HC-SR04 ultrasonic sensor
*  ROHS Stepper motor 28BYJ-48
*  ULN2003 Stepper motor driver
*  470 ohm resistor
*  330 ohm resistor
*  Bread board
*  Jumper wires 

## Raspberry Pi connections

Pin out:

| Physical pin | BCM/GPIO | Connected to                    |
|--------------|----------|---------------------------------|
| 1            |          | DS18b20 temperature: VCC (3.3V) |
| 2            |          | Relay board VCC (5V)            |
| 4            |          | PIR motion sensor 5V+           |
| 6            |          | Relay board GND                 |
| 7            | GPIO4    | DS18b20 temperature: SIG        |
| 9            |          | DS18b20 temperature: GND        |
| 11           | GPIO17   | Relay board: IN1                |
| 12           | GPIO18   | Status LED                      |
| 14           |          | Status LED GND                  |
| 16           | GPIO23   | PIR motion sensor               |
| 20           |          | PIR motion sensor GND           |
| 32           | GPIO12   | Stepper Coil A-1                |
| 33           | GPIO13   | Sonic distance echo             |
| 36           | GPIO16   | Stepper Coil A-2                |
| 37           | GPIO26   | Sonic distance trigger          |
| 38           | GPIO20   | Stepper Coil B-1                |
| 40           | GPIO21   | Stepper Coil B-2                |

Note: Power for the stepper motor and ultrasonic sensor come from an external source due to power limits of the Raspberry Pi.

Pinout of Raspberry PI:
<https://www.raspberrypi.org/documentation/usage/gpio/>

# Neo Pixel Strip

The goal of this section is to light up a neopixel strip using a Raspberry Pi and learn from the experiance.

# To Do's
* Change the pi's password.  Using the default password can cause problems with hackers taking it over.
* Change the patterns of light

## Warning:  Do *not* power the neopixel strip using the 5V pins on the Raspberry Pi.  Use a separate power source.

Number of LED's in my neo pixel strip:  100

How To article from Adafruit:  <https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage>

Do not run in virtual Python environment.

## Helloworld.py
A trival learning program

## Raspberry Pi info
IP address:  192.168.1.21
raspberry.local
user:  pi
pass:  raspberry

## Wiring

For pinout of the raspberry pi, see: <https://pinout.xyz/>

|Physical pin on Pi| Connects to             | Purpose        |
|------------------|-------------------------|----------------|
| 12               | D on the Neopixel strip | Communications |
| 6                | Ground or - on the power supply | Ties the ground voltages together |

### Power supply connections to the neopixel strip

5V+ to 5V+
Ground or - to ground and pin 6 on the Pi

## Use

1. Open a terminal and type:  ssh pi@192.168.1.21
1. type the password when prompted
1. cd Noepixels
1. sudo python3 testNeo.py

## To shutdown

1. control+c to stop the program running
1. sudo shutdown now

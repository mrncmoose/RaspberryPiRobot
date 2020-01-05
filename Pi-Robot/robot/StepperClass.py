'''A class to set up and control a given stepper motor
Fred. T. Dunaway
2019-12-17
'''

import RPi.GPIO as GPIO
import time
from stepper_constants import *

class Stepper:
    # Spec sheet may give a stride angle or the number of degrees rotation for a single pulse.
    # to get the number of steps to produce a full revolution, divide 360 by the stride angle .
    # i.e. 360/5.625 = 64  
    def __init__(self, GPIOpins = [12, 16, 20, 21], stepperMotorModel = '28BYJ-48'):
        self.GPIOpins = GPIOpins
        self.oneRevSteps = StepperMotors[stepperMotorModel]['oneRevSteps']
        self.maxRevsSec = StepperMotors[stepperMotorModel]['maxRevSec']
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.coil_A_1_pin = GPIOpins[0]
        self.coil_A_2_pin = GPIOpins[1]
        self.coil_B_1_pin = GPIOpins[2]
        self.coil_B_2_pin = GPIOpins[3]
         
        # Define advance sequence
        # as shown in manufacturers datasheet
        # this is for a ROHS 28BYJ-48
        self.Seq = StepperMotors[stepperMotorModel]['sequence']
        
        self.StepCount = len(self.Seq)
         
        GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_2_pin, GPIO.OUT)

    def turn_n_revolutions(self, nRevs=0, direction=FORWARD_DIRECTION, revsPerSec=0):
        if revsPerSec > self.maxRevsSec:
            print('Rev limiting to {0} revs/sec'.format(self.maxRevsSec))
            revsPerSec = self.maxRevsSec
        delay = 1/(revsPerSec*self.oneRevSteps * self.StepCount * 8)
        steps = int(nRevs * self.oneRevSteps * self.StepCount)
        if direction:
            self.forward(delay, steps)
        else:
            self.backwards(delay, steps)
    
    def setStep(self, w1, w2, w3, w4):
        GPIO.output(self.coil_A_1_pin, w1)
        GPIO.output(self.coil_A_2_pin, w2)
        GPIO.output(self.coil_B_1_pin, w3)
        GPIO.output(self.coil_B_2_pin, w4)
     
#Note:  delay is a float holding the number of seconds.  the sleep function is not highly accurate
    def forward(self, delay, steps):
        for i in range(steps):
            for j in range(self.StepCount):
                self.setStep(self.Seq[j][0], self.Seq[j][1], self.Seq[j][2], self.Seq[j][3])
                time.sleep(delay)
     
    def backwards(self, delay, steps):
        for i in range(steps):
            for j in reversed(range(self.StepCount)):
                self.setStep(self.Seq[j][0], self.Seq[j][1], self.Seq[j][2], self.Seq[j][3])
                time.sleep(delay)

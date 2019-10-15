'''
Created on Jul 6, 2019

@author: Mr NC Moose.  A.K.A. Fred T. Dunaway
'''
import RPi.GPIO as GPIO
import time


class SonicDistanceClass:
    '''
    A class to deal with required functions for a sonic distance sensor on a Raspberry Pi
    
    '''


    def __init__(self, TriggerPin = 4, EchoPin = 17, Tolerance = 0.1):
        '''
        Sets up the sensor including the GPIO pins the sonic sensor is connected to.
        ''' 
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        #set GPIO direction (IN / OUT)
        GPIO.setup(TriggerPin, GPIO.OUT)
        GPIO.setup(EchoPin, GPIO.IN)
        self.tolerance = Tolerance

    def GetDistance(self):
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
     
        StartTime = time.time()
        StopTime = time.time()
     
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
     
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
     
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
     
        return distance

    
    def AtDistance(self, distance, tolerance = 0.1):
        self.tolerance = tolerance
        currentDistance = self.GetDistance()
        if currentDistance <= distance - tolerance and currentDistance >= distance + tolerance:
            return True
        return False
    
            
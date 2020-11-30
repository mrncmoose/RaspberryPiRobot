import threading
from StepperClass import Stepper
from stepper_constants import *

#TODO:  Add turn command queue & pull movement commands from queue.
#See:   https://realpython.com/intro-to-python-threading/

def turn(stepper, revs, direction, revsSec):
    print('Turning starting.')
    stepper.turn_n_revolutions(nRevs=revs, direction=direction, revsPerSec=revsSec)
    print('Turning done.')
    
if __name__ == '__main__':
    #Use default pin and steps/one rev values
    stepper1 = Stepper()
#     print('Starting stepper thread')
#     t = threading.Thread(target=turn, args=(stepper1, 1.0, FORWARD_DIRECTION, 0.35))
#     t.start()
#     print('Done launching thread')
    print('Forward')
    stepper1.turn_n_revolutions(nRevs=0.25, direction=FORWARD_DIRECTION, revsPerSec=0.3)
    print("Backward.")
    stepper1.turn_n_revolutions(nRevs=0.5, direction=REVERSE_DIRECTION, revsPerSec=0.3)
    print('90 degrees forward')
    stepper1.turn_n_degrees(90, FORWARD_DIRECTION)
    print('90 degrees backward')
    stepper1.turn_n_degrees(90, REVERSE_DIRECTION)
    
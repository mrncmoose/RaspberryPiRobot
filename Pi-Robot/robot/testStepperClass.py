import threading
from StepperClass import Stepper
import stepper_constants as sc

#TODO:  Add turn command queue & pull movement commands from queue.
#See:   https://realpython.com/intro-to-python-threading/

def turn(stepper, revs, direction, revsSec):
    print('Turning starting.')
    stepper.turn_n_revolutions(nRevs=revs, direction=direction, revsPerSec=revsSec)
    print('Turning done.')
    
if __name__ == '__main__':
    #Use default pin and steps/one rev values
    stepper1 = Stepper()
    print('Starting stepper thread')
    t = threading.Thread(target=turn, args=(stepper1, 1.0, sc.FORWARD_DIRECTION, 0.35))
    t.start()
    print('Done launching thread')
#    stepper1.turn_n_revolutions(nRevs=0.25, direction=sc.FORWARD_DIRECTION, revsPerSec=5)
#     print("Backward.")
#     stepper1.turn_n_revolutions(nRevs=0.5, direction=sc.REVERSE_DIRECTION, revsPerSec=2)
    
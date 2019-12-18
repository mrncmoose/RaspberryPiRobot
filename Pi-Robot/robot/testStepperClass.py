from StepperClass import Stepper
import stepper_constants

if __name__ == '__main__':
    #Use default pin and steps/one rev values
    stepper1 = Stepper()
    stepper1.turn_n_revolutions(nRevs=0.25, direction=FORWARD_DIRECTION, revsPerSec=1)
    stepper1.turn_n_revolutions(nRevs=0.25, direction=REVERSE_DIRECTION, revsPerSec=1)
    
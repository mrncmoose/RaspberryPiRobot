#Holds values that are constants in the project
FORWARD_DIRECTION = True
REVERSE_DIRECTION = False

#A dict holding different sequences for different stepper motors.
#Format: key = stepper motor type/model, Value:  sequence array
StepperMotors = {'28BYJ-48': {'sequence': [[1,0,0,1],
                               [1,0,0,0],
                               [1,1,0,0],
                               [0,1,0,0],
                               [0,1,1,0],
                               [0,0,1,0],
                               [0,0,1,1],
                               [0,0,0,1]],
                               'oneRevSteps': 64
                               }
       }

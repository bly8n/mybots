import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self,robot,jointName):
        self.robot=robot
        self.jointName=jointName
        self.values=np.zeros(1000)
    def Set_Value(self,desiredAngle,robotId):
        self.robotId=robotId
        self.amplitude=c.amplitude
        self.frequency=c.frequency
        self.phaseOffset=c.phaseOffset
        if self.jointName == "Torso_BackLeg":
           self.frequency=self.frequency/2
        else:
            self.frequency=self.frequency
        pyrosim.Set_Motor_For_Joint(
            bodyIndex =self.robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 23)
        return desiredAngle
    

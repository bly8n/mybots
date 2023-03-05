import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self,robot,jointName):
        self.robot=robot
        self.jointName=jointName
        #self.robotId=robotId
        #self.robotId=p.loadURDF("body.urdf")
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
            targetPosition = self.amplitude * np.sin(self.frequency*desiredAngle*np.pi*2/100+ self.phaseOffset),
            maxForce = 23)
        self.values[desiredAngle]=np.sin(self.amplitude * np.sin(self.frequency*desiredAngle*np.pi*2/100+ self.phaseOffset))
        #if t==1000-1:
         #   print(self.jointName,self.values[t])
        return self.values[desiredAngle]
    #
    

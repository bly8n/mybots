from sensor import SENSOR
from motor import MOTOR
import numpy as np
import pyrosim.pyrosim as pyrosim
class ROBOT:
    def __init__(self,robotId):
        #self.motor=MOTOR()
        self.robotId=robotId
    def Prepare_To_Sense(self,t):
        self.sensor={}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensor[linkName] = SENSOR(self,linkName)
            #self.sensor[linkName].Get_Value(t)
            #self.sensor.append(sensor)
    def Sense(self,t):
        self.sensorvalues=[]
        for sensor in self.sensor.values():
            sensor_values=sensor.Get_Value(t)
            self.sensorvalues.append(sensor_values)
        return self.sensorvalues
    def Prepare_To_Act(self,t,robotId):
        self.motor={}
        for jointName in pyrosim.jointNamesToIndices:
            self.motor[jointName] = MOTOR(self,jointName)
            #self.motor[jointName].Set_Value(t,robotId)
    def Act(self,t,robotId):
        self.motorvalues=[]
        for motor in self.motor.values():
            motor_values=motor.Set_Value(t,robotId)
            self.motorvalues.append(motor_values)
        return self.motorvalues
    def Save_Values(self,t):
        sensorvalues = self.Sense(t)
        motorvalues = self.Act(t, self.robotId)
        np.save("data/sensorvalues",sensorvalues)
        np.save("data/targetangles",motorvalues)
            
            
        
        

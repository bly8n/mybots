from sensor import SENSOR
from motor import MOTOR
import numpy as np
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:
    def __init__(self,robotId):
        #self.motor=MOTOR()
        self.robotId=robotId
        self.nn=NEURAL_NETWORK("brain.nndf")
    def Prepare_To_Sense(self,t):
        self.sensor={}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensor[linkName] = SENSOR(self,linkName)
        return self.sensor
    def Sense(self,t):
        self.sensorvalues=[]
        self.sensor=self.Prepare_To_Sense(t)
        for sensor in self.sensor.values():
            sensor_values=sensor.Get_Value(t)
            self.sensorvalues.append(sensor_values)
        return self.sensorvalues
    def Prepare_To_Act(self):
        self.motor={}
        for jointName in pyrosim.jointNamesToIndices:
            self.motor[jointName] = MOTOR(self,jointName)
        return self.motor
    def Act(self,robotId):
        self.motorvalues=[]
        self.motor=self.Prepare_To_Act()
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName1= self.nn.Get_Motor_Neurons_Joint(neuronName)
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode()
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motor[jointName].Set_Value(desiredAngle, robotId)
                print(neuronName,jointName1,desiredAngle)
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()
    
            
            
        
        

import pyrosim.pyrosim as pyrosim
import numpy as np
class SENSOR:
    def __init__(self,robot,linkName):
        self.robot=robot
        self.linkName=linkName
        #print(self.linkName)
        self.values=np.zeros(1000)
    def Get_Value(self,t):
        #value=pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        self.values[t]=pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        return self.values[t]
        #if t==1000-1:
        #    print(self.linkName,self.values[t])#.append(self.values(t)))
        #self.linkName.append(self.values[i])
        
    
           
        

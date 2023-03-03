import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/100)
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
np.save("data/backLegSensorValues.npy",backLegSensorValues)
np.save("data/frontLegSensorValues.npy",frontLegSensorValues)
print(backLegSensorValues)
print(frontLegSensorValues) 
p.disconnect()


import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import matplotlib.pylab as plt
BackLeg_amplitude=np.pi/3
BackLeg_frequency=1
BackLeg_phaseOffset=0
FrontLeg_amplitude=np.pi/3
FrontLeg_frequency=1
FrontLeg_phaseOffset=0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
Back_targetAngles=np.zeros(1000)
Front_targetAngles=np.zeros(1000)
vector=np.zeros(1000)
x=np.zeros(1000)
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/240)
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    vector[i] = BackLeg_amplitude * np.sin(BackLeg_frequency* i*np.pi*2/100+ BackLeg_phaseOffset)
    x[i] = FrontLeg_amplitude * np.sin(FrontLeg_frequency * i*np.pi*2/100 + FrontLeg_phaseOffset)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = vector[i],
        maxForce = 23)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition =x[i],
        maxForce = 23)
    Back_targetAngles[i]=np.sin(vector[i])
    Front_targetAngles[i]=np.sin(x[i])
np.save("data/backLegSensorValues.npy",backLegSensorValues)
np.save("data/frontLegSensorValues.npy",frontLegSensorValues)
np.save("data/Back_targetAngles.npy",Back_targetAngles)
np.save("data/Front_targetAngles.npy",Front_targetAngles)
print(backLegSensorValues)
print(frontLegSensorValues) 
p.disconnect()

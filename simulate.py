import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
#import constants as c

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
p.loadSDF("boxes.sdf")
#pyrosim.Prepare_To_Simulate(robotId)

#exit()
#np.linspace(-np.pi/4, np.pi/4,1000)
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/240)
    #c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #c.vector[i] = c.BackLeg_amplitude * np.sin(c.BackLeg_frequency* i*np.pi*2/100+c.BackLeg_phaseOffset)
    #c.x[i] = c.FrontLeg_amplitude * np.sin(c.FrontLeg_frequency * i*np.pi*2/100 +c.FrontLeg_phaseOffset)
    #pyrosim.Set_Motor_For_Joint(
     #   bodyIndex = robotId,
      #  jointName = b'Torso_BackLeg',
       # controlMode = p.POSITION_CONTROL,
        #targetPosition =c.vector[i],#random.uniform(-np.pi/2,np.pi/2),
        #maxForce = 23)
    #pyrosim.Set_Motor_For_Joint(
     #   bodyIndex = robotId,
      #  jointName = b'Torso_FrontLeg',
       # controlMode = p.POSITION_CONTROL,
       # targetPosition =c.vector[i],#random.uniform(-np.pi/2,np.pi/2),
        #maxForce = 23)
    #c.Back_targetAngles[i]=np.sin(c.vector[i])
    #c.Front_targetAngles[i]=np.sin(c.x[i])
    #print(i)
#np.save("data/backLegSensorValues.npy",backLegSensorValues)
#np.save("data/frontLegSensorValues.npy",frontLegSensorValues)
#np.save("data/Back_targetAngles.npy",Back_targetAngles)
#np.save("data/Front_targetAngles.npy",Front_targetAngles)
#exit()
#x = np.linspace(-np.pi/2, np.pi/2, 500)
#plt.plot(x,targetAngles)
#plt.show()
#print(backLegSensorValues)
#print(frontLegSensorValues) 
p.disconnect()


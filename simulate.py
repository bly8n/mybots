import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadSDF("Box.sdf")
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/240)
p.disconnect()

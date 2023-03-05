from world import WORLD
from robot import ROBOT
from sensor import SENSOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time
import numpy as np
import random
class SIMULATION:
    def __init__(self):
        self.world=WORLD()
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.robotId = p.loadURDF("body.urdf")
        self.robot=ROBOT(self.robotId)
        pyrosim.Prepare_To_Simulate(self.robotId)
        #self.robot.Prepare_To_Sense()
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            time.sleep(1/240)
            self.robot.Prepare_To_Sense(i)
            self.robot.Think()
            self.robot.Prepare_To_Act(i,self.robotId)
            self.robot.Save_Values(i)
            
    def __del__(self):
        p.disconnect()

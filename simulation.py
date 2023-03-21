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
import sys
class SIMULATION:
    def __init__(self,directOrGUI,solutionID):
        self.world=WORLD()
        self.solutionID=solutionID
        self.directOrGUI=directOrGUI
        if self.directOrGUI=='DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        elif self.directOrGUI=='GUI':
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.robotId = p.loadURDF("body.urdf")
        self.robot=ROBOT(self.robotId,solutionID)
        pyrosim.Prepare_To_Simulate(self.robotId)
        #self.robot.Prepare_To_Sense()
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
        
    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            #if self.directOrGUI=='GUI':
            time.sleep(1/100)
            self.robot.Sense(i)
            self.robot.Think()
            #self.robot.Save_Values(i)
            self.robot.Act(self.robotId)
    def Get_Fitness(self):
        self.robot.Get_Fitness(self.robotId)
            
    def __del__(self):
        p.disconnect()

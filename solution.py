import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
class SOLUTION:
    def __init__(self,myID):
        self.weight=np.random.rand(3,2)
        self.weights = self.weight*2-1
        self.myID=myID
    def Start_Simulation(self,mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        if mode=="GUI":
           os.system("python simulate.py GUI"+str(self.myID)+"&")
        else:
           os.system("python simulate.py DIRECT"+str(self.myID)+"&")
    def Wait_For_Simulation_To_End(self,mode):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
            os.rename("tmp"+str(self.myID)+".txt" , "fitness"+str(self.myID)+".txt")
        f = open("fitness"+str(self.myID)+".txt", "r")
        fitness_str = f.read()
        f.close()
        os.remove("fitness"+str(self.myID)+".txt")
        self.fitness = float(fitness_str)
        return self.fitness
    def Evaluate(self,solutions):
        for parent in solutions.values():
            parent.Start_Simulation("GUI")
            time.sleep(2)
            parent.fitness=parent.Wait_For_Simulation_To_End("GUI")
            print(parent.fitness)
        return parent.fitness
    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1
    def Set_ID(self,myID):
        self.myID=myID
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-1,1,0.5] , size=[1,1,1])
        pyrosim.End()
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1,1,1])
        pyrosim.End()
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range(3):
            for currentColumn in range(2):
                weight = 2.0 * random.random() - 1.0
                pyrosim.Send_Synapse(sourceNeuronName=currentRow , targetNeuronName=currentColumn +3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

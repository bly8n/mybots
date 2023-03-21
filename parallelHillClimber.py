from solution import SOLUTION
import constants as c
import copy
import os
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #os.remove("brain*.nndf")
        #os.remove("fitness*.text")
        self.parents={}
        self.nextAvailableID=0
        for i in range(c.populationSize):
            self.parents[i]=SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1
            
    def Evolve(self,mode):
        for parent in self.parents.values():
            parent.Evaluate(self.parents)
            for currentGeneration in range(c.numberOfGenerations):
                self.Evolve_For_One_Generation(mode)
    def Evolve_For_One_Generation(self,mode):
        self.Spawn()
        self.Mutate()
        for key,child in self.children.items():
            self.children[key].fitness=self.children[key].Evaluate(self.children)
            print(self.children[key].fitness)
        self.Select()
    def Spawn(self):
        self.children={}
        for key,parent in self.parents.items():
            self.children[key]=copy.deepcopy(parent)
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        return self.children
    def Mutate(self):
        for key,parent in self.parents.items():
            self.children[key].Mutate()
    def Select(self):
        for key, parent in self.parents.items():
            if self.parents[key].fitness>self.children[key].fitness:
               self.parents[key]=self.children[key]
    def Show_Best(self):
        for key, parent in self.parents.items():
            self.parents[key].Start_Simulation('GUI')

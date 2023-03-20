from solution import SOLUTION
import constants as c
import copy
class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
    def Evolve(self,mode):
        self.parent.fitness=self.parent.Evaluate(mode)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(mode)
    def Evolve_For_One_Generation(self,mode):
        self.Spawn()
        self.Mutate()
        self.child.fitness=self.child.Evaluate(mode)
        self.Select()
    def Spawn(self):
        self.child=copy.deepcopy(self.parent)
        return self.child
    def Mutate(self):
        self.child.Mutate()
    def Select(self):
        if self.parent.fitness>self.child.fitness:
           self.parent=self.child
    def Show_Best(self):
        self.parent.Evaluate('GUI')

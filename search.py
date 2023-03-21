import os
import time
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve('GUI')
phc.Show_Best()
#for i in range(5):
    #os.system("python generate.py")
    #time.sleep(2)
    #os.system("python simulate.py")
    #

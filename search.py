import os
import time
from hillclimber import HILL_CLIMBER
hc = HILL_CLIMBER()
hc.Evolve('DIRECT')
hc.Show_Best()
#for i in range(5):
    #os.system("python generate.py")
    #time.sleep(2)
    #os.system("python simulate.py")
    #

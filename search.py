import os
import time
for i in range(2):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")
    time.sleep(5)

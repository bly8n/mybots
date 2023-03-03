import numpy as np
import matplotlib.pyplot as plt
backLegSensorValues = np.load("data/backLegSensorValues.npy",allow_pickle=True)
frontLegSensorValues = np.load("data/frontLegSensorValues.npy",allow_pickle=True)
#Back_targetAngles = np.load("data/Back_targetAngles.npy",allow_pickle=True)
#Front_targetAngles = np.load("data/Front_targetAngles.npy",allow_pickle=True)
print(backLegSensorValues)
print(frontLegSensorValues)

plt.plot(backLegSensorValues,linewidth=1.5)
plt.plot(frontLegSensorValues,linewidth=1.5)
#plt.plot(Back_targetAngles,linewidth=3)
#plt.plot(Front_targetAngles,linewidth=1.5)
plt.title("plot of front/back sensor values vs time")
plt.xlabel("time(step)")
plt.ylabel("front/back sensor values")
plt.legend((r'back', r'front'), loc='upper right')
plt.show()

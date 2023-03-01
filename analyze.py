import numpy as np
import matplotlib.pyplot as plt
backLegSensorValues = np.load("data/backLegSensorValues.npy",allow_pickle=True)
frontLegSensorValues = np.load("data/frontLegSensorValues.npy",allow_pickle=True)
print(backLegSensorValues)
print(frontLegSensorValues)

plt.plot(backLegSensorValues,linewidth=1.5)
plt.plot(frontLegSensorValues,linewidth=1.5)
plt.title("plot of front/back sensor values vs time")
plt.xlabel("time(step)")
plt.ylabel("front/back sensor values")
plt.legend((r'back', r'front'), loc='upper right')
plt.show()

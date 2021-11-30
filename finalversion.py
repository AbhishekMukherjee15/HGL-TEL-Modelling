# Prefix:
# 1. The centerline of the tube is considered to be the datum for this system

import matplotlib.pyplot as plt

density = 1000  # in kg/m^3
gravity = 9.81  # in m/s^2

pzHeights = [20, 18.5, 15.5, 6.7, 11.8, 15, 18]  # in cm
sectionDiameters = [30, 24, 20, 16, 20, 24, 30]  # in cm

tankArea = 0.077  # in m^2
tankReadings = [8.5, 19]  # in cm
flowTime = 30  # in sec

flowVolume = ((tankReadings[1]-tankReadings[0])/100)*tankArea  # in m^3
flowRate = flowVolume/flowTime  # in m^3/sec

hgl = []
for reading in pzHeights:
    hgl.append(reading/100)


tel = []
for i in range(0, 7):
    velocity = flowRate/(3.1415*(sectionDiameters[i]/(2*100))**2)
    velhead = velocity/(2*gravity)
    tel.append(hgl[i]+velhead)

plt.plot(range(1, 8), hgl, label="HGL")
plt.plot(range(1, 8), tel, "--", label="TEL")
plt.ylabel("Distance from the centerline of the tube (in metres)")
plt.xlabel("Piezometer Index [1-6]")
plt.legend()
plt.title("HGL and TEL")
plt.show()

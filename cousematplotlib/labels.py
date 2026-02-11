import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.array([2023,2024,2025,2026])
y1=np.array([15,25,30,20])
y2=np.array([17,2,38,5])
y3=np.array([13,15,20,30])
plt.title("Class size",size=25,fontsize=20,
                       family="arial",
                       fontweight="bold",
                       color="#154154")
plt.xlabel('year',fontsize=13,fontweight="bold")
plt.ylabel('data',fontsize=13,fontweight="bold")

plt.tick_params(axis="both",colors="#154154")
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.xticks(x)

plt.show()
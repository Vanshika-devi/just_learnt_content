import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.array(['class 9','class 10','class 11','class 12'])
y=np.array([130,150,110,120])
y1=np.array([110,140,160,130])
styles=dict(
    markersize=10,
    marker="o",
    markeredgecolor="white",
    linestyle="solid"
)
plt.tick_params(axis='x',color="blue")
plt.tick_params(axis='y',color="green")
plt.tick_params(axis='both',color="yellow")

plt.xlabel('class',fontweight="bold",size=12,color="#0b1654")
plt.ylabel('no of students',fontweight="bold",size=12,color="#730914")
plt.grid(axis="both",linestyle="dotted",linewidth=2,color='darkgray')
plt.plot(x,y,color="black",**styles)
plt.plot(x,y1,color="green",**styles)
plt.xticks(x)
plt.yticks(y)
plt.show()

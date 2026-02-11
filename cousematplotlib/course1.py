import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
x=np.array([2023,2024,2025,2026])
y=np.array([15,25,30,20])
y1=np.array([17,23,38,5])
line_style=dict(
         marker=".",
         markersize=30,#markersize can be also written as the ms
         markerfacecolor="cyan",#markerfacecolor can be written as mfc also
         markeredgecolor="white",
         linestyle="dashed",
         linewidth=2,
         color="red")

plt.plot(x,y,marker=".",
         markersize=30,#markersize can be also written as the ms
         markerfacecolor="cyan",#markerfacecolor can be written as mfc also
         markeredgecolor="white",
         linestyle="dashed",
         linewidth=2,
         color="red")
plt.plot(x,y1,color="yellow",**line_style)
plt.show()
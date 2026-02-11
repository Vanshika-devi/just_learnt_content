import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#grid()=helps make plots easier to read by adding by adding reference lines
x=[1,2,3,4,5]
y=[5,10,15,20,25]
plt.grid(axis='both',linewidth=2,color="lightgray",linestyle="dotted")
plt.plot(x,y)
plt.show()
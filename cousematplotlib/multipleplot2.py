import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
z1=np.linspace(0,5,7)
z2=z1**2
plt.plot(z1,z2)
plt.subplot(1,2,1)
plt.plot(z1,z2,'r')
plt.subplot(1,2,2)
plt.plot(z1,z2,'b')
plt.show()
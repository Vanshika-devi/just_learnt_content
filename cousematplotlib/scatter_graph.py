import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#scattar graph=show the relationships between the two variables 
#helps to identify a correlation(+,-,None)
# Example:study hours vs.test scores
x=np.array([0,1,1,2,3,4,5,6,7,7,8])# hours studied
y=np.array([55,60,65,62,68,70,75,78,82,85,87])# grades

x1=np.array([0,1,2,2,3,4,5,6,7,8,8])# hours studied
y1=np.array([50,58,65,70,72,78,83,88,92,95,97])

plt.scatter(x,y,color='blue',
            alpha=0.9,
            s=50,
            label="class a")#the alpha keyword is for the transperancy of the scattered points
plt.scatter(x1,y1,color='red',
            alpha=0.9,
            s=50,
            label="class b")#the alpha keyword is for the transperancy of the scattered points
plt.grid(axis='both')
plt.title('Test scores')
plt.xlabel('hours studied')
plt.ylabel('marks obtained')
plt.legend()
plt.show()
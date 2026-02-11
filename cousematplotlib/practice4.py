import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
p1=np.array([12,13,9,5,10,4,3,2])
p2=np.array([89,92,82,68,85,50,46,40])

p3=np.array([17,15,11,7,12,4,5,2])
p4=np.array([97,94,85,73,89,50,52,40])
plt.grid(axis="both")
style=dict(
    color="blue",
    weight='bold',
    family="Arial",
    size=12
)
plt.scatter(p1,p2,color='red',
            alpha=0.9,
            s=25,
            label="class a")
plt.scatter(p3,p4,color='blue',
            alpha=0.9,
            s=25,
            label="class b")

plt.xlabel('hours',**style)
plt.ylabel('grade obtained',**style)
plt.title('Analysis on class')
plt.legend()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#bar chart= circular chart divided into slices to show percentages of the total
#good for vizualizing istribution among categories
categories=np.array(['freshman','sophormes','junior','seniors'])
values=np.array([300,250,275,225])
colors=np.array(['red','yellow','blue','green'])
plt.pie(values,
        labels=categories,
        autopct='%1.1f%%',
        colors=colors,
        explode=[0,0,0,0.1],
        shadow=True,
        startangle=-180)
plt.title('college data')
plt.show()
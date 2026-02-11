import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
categories=np.array(['students','doctors','engineer','designer','model'])
values=np.array([110,46,56,22,5])
plt.pie(values,
        labels=categories,
        autopct='%1.1f%%',
        colors=['yellow','green','red','purple','blue'],
        shadow=True,
        explode=[0,0,0.1,0,0],
        startangle=90)
plt.show()
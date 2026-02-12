import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#histograms=a visual representation of the ditribution of quantative data. 
#They group values into the bins(intervals)
#and counts how amny falls intp each range
scores=np.random.normal(loc=80,scale=10,size=100)
scores=np.clip(scores,0,100)
plt.hist(scores,bins=10,
         color='lightgreen',
         edgecolor='black')
plt.xlabel('Scores')
plt.ylabel('no of students')
plt.title('Exam scores')
plt.show()
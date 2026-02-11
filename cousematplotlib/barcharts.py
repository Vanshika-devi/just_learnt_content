import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#bar chart=compare categories of data by represetimg ach catgory with a bar
categores=np.array(['grains','fruit','vegatables','protein','dairy','sweets'])
values=np.array([4,3,2,5,3,1])
styles=dict(
    color="red",
    weight="bold"
)
plt.grid(axis='y')
plt.bar(categores,values,color="yellow")
# plt.barh(categores,values)for the horizontal barchart
plt.title('daily consumpation')
plt.xlabel('categories',**styles)
plt.ylabel('amount',**styles)
plt.show()
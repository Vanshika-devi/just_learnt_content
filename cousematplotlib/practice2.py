import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
year=np.array([2024,2025,2026,2027])
std=np.array([120,130,170,150])
style=dict(
    color='red',
    weight='bold',
    family='arial'
)
plt.bar(year,std,color='blue')
plt.grid(axis='y')
plt.xlabel('year of the student',**style)
plt.ylabel('students in the class',**style)
plt.show()
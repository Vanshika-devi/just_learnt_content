import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/Dell/3D Objects/project-1/students_marks_analyzer project/StudentsPerformance.csv')
type_count=df['math score'].value_counts(ascending=True)
plt.barh(type_count.index,type_count.values,color="cyan",edgecolor="black")
plt.xlabel('No of student')
plt.ylabel('marks in maths')
plt.title('maths analysis')
plt.show()
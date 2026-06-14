import numpy as np 
from scipy import stats
data=[10,12,14,15,16,18,20,22,24,150]
z_score=stats.zscore(data)
threshold=2.5
outliers=[]
for i in range(len(data)):
    if abs(z_score[i])>threshold:
        outliers.append(data[i])
print("data:",data)
print("z_score:",z_score)
print("outlier:",outliers)
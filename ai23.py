import numpy as np         
data = np.array([10, 12, 14, 15, 16, 18, 20, 22, 24])
data_min=np.min(data)
data_max=np.max(data)
normalized_data=(data-data_min)/(data_max-data_min)
print("orginal data:",data)
print("minimum value:",data_min)
print("maximum value:",data_max)
print("normalized data:",normalized_data)
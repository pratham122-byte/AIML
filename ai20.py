import numpy as np
from sklearn.preprocessing import MinMaxScaler
data = np.array([10, 12, 14, 15, 16, 18, 20, 22, 24]).reshape(-1, 1)
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)
print("Original Data:")
print(data.flatten())
print("\nMin-Max Normalized Data:")
print(normalized_data.flatten())
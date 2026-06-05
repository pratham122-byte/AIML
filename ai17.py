import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
data = {
    'Age': [20, 25, np.nan, 30, np.nan],
    'Salary': [30000, 40000, 50000, np.nan, 60000]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
imputer = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = imputer.fit_transform(df[['Age', 'Salary']])
print("\nData after handling missing values:")
print(df)
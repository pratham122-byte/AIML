import numpy as np
import pandas as pd
from scipy import stats
data = {
    'Marks': [35, 36, 37, 38, 39, 40, 95, 41, 42, 43]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
z_scores = stats.zscore(df['Marks'])
threshold = 3
outliers = df[np.abs(z_scores) > threshold]
print("\nOutliers using Z-score:")
print(outliers)
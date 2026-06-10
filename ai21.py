import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    'House_Size': [500, 800, 1000, 1200, 1500, 1800],
    'House_Price': [150000, 200000, 250000, 300000, 360000, 400000]
}
df = pd.DataFrame(data)
X = df[['House_Size']]
y = df['House_Price']
model = LinearRegression()
model.fit(X, y)
new_house_size = [[1400]]
predicted_price = model.predict(new_house_size)
print("House Size (sq ft):", new_house_size[0][0])
print("Predicted House Price:", predicted_price[0])
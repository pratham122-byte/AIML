import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8],
    'Marks': [10, 20, 30, 40, 50, 60, 70, 80]
}
df = pd.DataFrame(data)
X = df[['Hours_Studied']]  
y = df['Marks']             
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Training Data:")
print(X_train)
print("\nTesting Data:")
print(X_test)
print("\nPredicted Marks:")
print(y_pred)
print("\nMean Squared Error:")
print(mean_squared_error(y_test, y_pred))

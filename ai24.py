import numpy as np         
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
x=np.array([800,1000,1200,1500,1800]).reshape(-1,1)
y=np.array([120,150,180,210,250])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
y_pred1=model.predict([[300]])
print("test data(x_test):",x_test)
print("actual price(y_test):",y_test)
print("predicted price(y_pred):",y_pred)
print("slope(coefficient):",model.coef_)
print("intercept:",model.intercept_)
print("price value for area 300sqft:",y_pred1)
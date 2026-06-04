import numpy as np                      
from sklearn.model_selection import train_test_split
x=np.array([800,1000,1200,1500,1800]).reshape(-1,1)
y=np.array([120,150,180,210,250])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print("X_train:",x_train)
print("y_train:",y_train)
print("x_test:",x_test)
print("y_test:",y_test)

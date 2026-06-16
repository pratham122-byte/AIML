import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
x_mean = np.mean(x)
y_mean = np.mean(y)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
m = numerator / denominator
c = y_mean - m * x_mean
y_pred = m * x + c
plt.scatter(x, y, label="Data Points")
plt.plot(x, y_pred, label="Best Fit Line")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Best Fit Regression Line")
plt.legend()
plt.show()

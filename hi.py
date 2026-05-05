import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random

x = np.linspace(10, 100, 50)
y = x + np.random.randint(5,100, 50)
line_model = stats.linregress(x,y)
slope = line_model[0]
intercept = line_model[1]
plt.scatter(x,y)
print (line_model)

fit_line = slope * x + intercept  # type: ignore
plt.plot (x, fit_line, label = "best fit line")
plt.legend()
plt.show()
print("Slope:", slope)
print("Intercept:", c)




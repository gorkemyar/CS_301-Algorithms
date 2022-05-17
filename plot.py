import numpy as np;
from matplotlib import pyplot as plt

arrX=np.array([6.890296936035156e-05, 4.1961669921875e-05, 7.200241088867188e-05, 0.00016307830810546875, 0.00019502639770507812, 0.0003287792205810547])
arrY=np.array([2,3,4,5,6,7])
plt.xlabel("Time")
plt.ylabel("Graph Size")
plt.title("Finding Shortest Path")
plt.plot(arrX,arrY,)

plt.show()
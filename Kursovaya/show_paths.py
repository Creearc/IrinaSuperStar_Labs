import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from csv_functions import load_coords

fig = plt.figure()
ax = plt.axes(projection='3d')

cols = 'rgbcmy'

for ind in range(len(os.listdir("paths"))):
    points = load_coords(ind)
    for i in range(2, len(points)):
        ax.plot((points[i - 1][0], points[i][0]),
                (points[i - 1][1], points[i][1]),
                (points[i - 1][2], points[i][2]),
                color=cols[(ind + 1) % 6])

# for i in range(50):
#    ax.scatter(points[i][0], points[i][1], points[i][2], s = 5)

plt.show()


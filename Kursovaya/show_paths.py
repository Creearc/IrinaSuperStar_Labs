import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from csv_functions import load_coords

def sred(elem):
    sx, sy, sz = 0.0, 0.0, 0.0
    ln = len(elem)
    if ln > 0:
        for k in range(ln):
            sx += elem[k][0]
            sy += elem[k][1]
            sz += elem[k][2]
        return (sx/ln, sy/ln, sz/ln)
    else:
        return (0.0, 0.0, 0.0)
    

fig = plt.figure()
ax = plt.axes(projection='3d')

cols = 'rgbcmy'
r = 30

for ind in range(len(os.listdir("paths"))):
    points = load_coords(ind)
    (x, y, z) = points[0]
    for i in range(r, len(points)):
        (x1, y1, z1) = sred(points[i - r : i + r + 1])
        ax.plot((x, x1),
                (y, y1),
                (z, z1),
                color=cols[(ind + 5) % 6])
        (x, y, z) = (x1, y1, z1)




plt.show()


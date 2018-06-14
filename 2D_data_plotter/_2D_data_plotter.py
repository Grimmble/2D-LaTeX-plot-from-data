import numpy as np
import matplotlib.pyplot as plt
from pylab import *



# LaTex Interpreter
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Declare x/y as empty arrays
x, y = [], []
n = 0.0

# Append data values from file to y
with open("test_data.txt", "r") as data_buffer:
    y_raw = []
    for line in data_buffer:
        y_raw = line.split()
        y.append(float(y_raw[0]))

# x-array in increments of 1 with same length as y
for i in range(len(y)):
    x.append(n)
    n += 1.0

# Plot results
plt.figure(figsize=(9,6))
plt.plot(x, y, linewidth=3.0, color="orange")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("2D plot from .txt data: $y \in (0,9)$", fontsize=18.0)
plt.show()
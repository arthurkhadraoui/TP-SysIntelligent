import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D

inputs = [[0,0],[0,1],[1,0],[1,1]]
outputs = [0,0,0,1]

erreur = []

comp = []

surfaceerreur = np.zeros((11,11))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X = np.arange(-5, 6, 1)
Y = np.arange(-5, 6, 1)
X, Y = np.meshgrid(X, Y)


for w1 in range(-5,6):
    for w2 in range(-5,6):
        etot=0
        for i in range(4):
            sol=w1*inputs[i][0]+w2*inputs[i][1]

            etot += 0.5*(sol-outputs[i])*(sol-outputs[i])
        surfaceerreur[w1+5][w2+5]=etot

surf = ax.plot_surface(X, Y,surfaceerreur,cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.show()
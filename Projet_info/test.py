import numpy as np
import matplotlib.pyplot as plt



laby = [[('N', 'E'), ('N', 'W')],  #les lignes sont inversées pour faciliter le tracé
        [('S', 'E'), ('S', 'W')]]

laby2 = [[('N',), ('N', 'E'), ('E', 'W'), ('E', 'W'), ('E', 'W'), ('N', 'W')],
 [('N', 'S'), ('S', 'E'), ('N', 'W'), ('N', 'E'), ('W',), ('N', 'S')],
 [('N', 'S', 'E'), ('N', 'W'), ('N', 'S'), ('S', 'E'), ('E', 'W'), ('S', 'W')],
 [('N', 'S'), ('N', 'S'), ('S', 'E'), ('N', 'W'), ('N', 'E'), ('N', 'W')],
 [('S',), ('S', 'E'), ('E', 'W'), ('S', 'E', 'W'), ('S', 'W'), ('S',)]]

for i in range(len(laby2)):
        for j in range(len(laby2[i])):
                dir = laby2[i][j]
                if 'N' not in dir:
                        plt.plot([j-0.5, j+0.5],[i+0.5, i+0.5], 'blue')
                if 'S' not in dir:
                        plt.plot([j-0.5, j+0.5], [i-0.5, i-0.5], 'blue')
                if 'E' not in dir:
                        plt.plot([j+0.5, j+0.5], [i-0.5, i+0.5], 'blue')
                if 'W' not in dir:
                        plt.plot([j-0.5, j-0.5], [i-0.5, i+0.5], 'blue')


plt.show()
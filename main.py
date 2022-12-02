import matplotlib.pyplot as plt

laby = [[('N', 'E'), ('W',), ('N', 'E'), ('W',)],
        [('N', 'S'), ('N', 'E'), ('N', 'S', 'W'), ('N',)],
        [('N','S', 'E'), ('N', 'S', 'W'), ('S',), ('N', 'S')],
        [('S',), ('S', 'E'), ('E', 'W'), ('S', 'W')]]



for i in range(len(laby)):
        for j in range(len(laby[i])):
                dir = laby[i][j]
                if 'N' not in dir:
                        plt.plot([j, j+1],[i+1, i+1], 'blue')
                if 'S' not in dir:
                        plt.plot([j, j+1], [i, i], 'blue')
                if 'E' not in dir:
                        plt.plot([j+1, j+1], [i, i+1], 'blue')
                if 'W' not in dir:
                        plt.plot([j, j], [i, i+1], 'blue')




plt.show()
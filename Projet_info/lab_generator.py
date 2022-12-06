import numpy as np
import matplotlib.pyplot as plt


class Case:
    def  __init__(self,x,y):
        self.x = x
        self.y = y
        self.Nord = False
        self.South = False
        self.Est = False
        self.West = False
        self.IsEntrence = False
        self.IsExit = False
        self.cote=[self.Nord,self.South,self.Est,self.West]

    def __repr__(self):
        return "Case ("+("N" if self.cote[0] else "") + ("S" if self.cote[1] else "") + ("E" if self.cote[2] else "") + ("W" if self.cote[3] else "") + ")"

class labyrinth:
    def __init__(self, a: int, b: int):
        self.lines = a
        self.columns = b
        self.laby = [[Case(j,i) for i in range(self.columns)] for j in range(self.lines)]

    def __repr__(self):
        return f"labyrinth ({self.lines} lines, {self.columns} columns) [{self.lab.__repr__()}]"


def show_laby(lab):
    for i in range(len(lab.laby)-1,0,-1):
        for j in range(len(lab.laby[i])-1,0,-1):
                dir = lab.laby[i][j].cote
                if  dir.Nord == False:
                        plt.plot([j, j+1],[i+1, i+1], 'blue')
                if 'S' not in dir:
                        plt.plot([j, j+1], [i, i], 'blue')
                if 'E' not in dir:
                        plt.plot([j+1, j+1], [i, i+1], 'blue')
                if 'W' not in dir:
                        plt.plot([j, j], [i, i+1], 'blue')
    plt.show()



Lab = labyrinth(5,5)
for x in Lab.laby:
    for y in x:
        Lab.Nord = True
        Lab.West = True
        Lab.Est = True

show_laby(Lab)

#fonction
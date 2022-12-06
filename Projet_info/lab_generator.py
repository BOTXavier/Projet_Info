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


    def show_laby(self):
        for i in range(len(self.laby)-1,0,-1):
            for j in range(len(self.laby[i])-1):
                dir = self.laby[i][j]
                if  dir.Nord == False:
                    plt.plot([j, j+1],[i+1, i+1], 'blue')
                if dir.South == False:
                    plt.plot([j, j+1], [i, i], 'blue')
                if dir.Est == False:
                    plt.plot([j+1, j+1], [i, i+1], 'blue')
                if dir.West == False:
                    plt.plot([j, j], [i, i+1], 'blue')
        plt.show()


    def __repr__(self):
        return f"labyrinth ({self.lines} lines, {self.columns} columns) [{self.lab.__repr__()}]"


Lab = labyrinth(5,5)
Lab.laby[2][0].South = True


Lab.show_laby()

import matplotlib.pyplot as plt


class Case:
    def  __init__(self,x,y):
        self.x = x
        self.y = y
        self.North = False
        self.South = False
        self.Est = False
        self.West = False
        self.IsEntrence = False
        self.IsExit = False
        self.cote=[self.North,self.South,self.Est,self.West]

    def __repr__(self):
        return "Case ("+("N" if self.cote[0] else "") + ("S" if self.cote[1] else "") + ("E" if self.cote[2] else "") + ("W" if self.cote[3] else "") + ")"

class labyrinth:
    def __init__(self, a: int, b: int):
        self.lines = a
        self.columns = b
        self.laby = [[Case(j,i) for i in range(self.columns)] for j in range(self.lines)]


    def show_laby(self):
        plt.plot([-0.5,self.columns+0.5],[-0.5,-0.5],'black')
        plt.plot([-0.5,self.columns+0.5],[self.lines+0.5,self.lines+0.5],'black')
        plt.plot([-0.5,-0.5],[-0.5,self.lines+0.5],'black')
        plt.plot([self.columns+0.5,self.columns+0.5],[-0.5,self.lines+0.5],'black')
        for i in range(len(self.laby)-1,0,-1):
            for j in range(len(self.laby[i])-1):
                dir = self.laby[i][j]
                if  dir.North == True:
                    plt.plot([j-0.5, j+0.5],[i+0.5, i+0.5], 'blue')
                if dir.South == True:
                    plt.plot([j-0.5, j+0.5], [i-0.5, i-0.5], 'blue')
                if dir.Est == True:
                    plt.plot([j+0.5, j+0.5], [i-0.5, i+0.5], 'blue')
                if dir.West == True:
                    plt.plot([j-0.5, j-0.5], [i-0.5, i+0.5], 'blue')
        plt.show()


    def __repr__(self):
        return f"labyrinth ({self.lines} lines, {self.columns} columns) [{self.laby.__repr__()}]"


Lab = labyrinth(5,5)
Lab.laby[2][0].South = True
Lab.laby[3][0].Est = True
Lab.laby[3][1].North = True
Lab.laby[4][1].West = True
Lab.laby[0][4].Est = True
Lab.laby[2][1].North = True
Lab.laby[1][1].Est = True

print(Lab.laby)


Lab.show_laby()

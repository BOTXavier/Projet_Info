import matplotlib.pyplot as plt


class Case:
    def  __init__(self,x,y):
        self.x = x
        self.y = y
        self.North = True
        self.South = True
        self.Est = True
        self.West = True
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
        """
        This function print the Lab with matplotlib
        """
        plt.plot([-0.5,self.columns-0.5],[-0.5,-0.5],'black')
        plt.plot([-0.5,self.columns-0.5],[self.lines-0.5,self.lines-0.5],'black')
        plt.plot([-0.5,-0.5],[-0.5,self.lines-0.5],'black')
        plt.plot([self.columns-0.5,self.columns-0.5],[-0.5,self.lines-0.5],'black')

        for i in range(len(self.laby)-1,-1,-1):
            for j in range(len(self.laby[i])):
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


def readlab(file):
    """
    Read a .txt type with format :
    lines columns
    [N,S,E,W,Entrance,Exit] [...]... * columns
    .
    .
    .
    *lines
    End 
    """
    with open(file,'r') as f:
        l = None

        while l != "End":
            for line in f:
                l = line
                if len(l) ==2:
                    lines = l[0]
                    columns = l[1]
                    lab = labyrinth(lines,columns)
                    i = lines
                    j = 0
                else:
                    l = l.split()
                    for x in l:
                        while i >= 0:
                            while j <= columns:
                                case_ij = lab.laby[i][j]
                                if 'N' not in l:
                                    case_ij.North = False
                                elif 'S' not in l:
                                    case_ij.South = False
                                elif 'E' not in l:
                                    case_ij.Est = False
                                elif 'W' not in l:
                                    case_ij.West = False

                                if 'Entrance' in l:
                                    case_ij.IsEntrence = True
                                elif 'Exit' in l:
                                    case_ij.IsExit = True
                                j +=1
                            i -=1
    return lab

                   
f = 'Labyrinth.txt'
Lab = readlab(f)

print(Lab)
Lab.show_laby()

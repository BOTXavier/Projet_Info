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
    (NSEWIO) (...)... * columns
    .
    .
    .
    *lines
    End 
    """
    with open(file,'r') as f:
        l = f.readline().split()  
        lines = int(l[0])
        columns = int(l[1])
        lab = labyrinth(lines,columns)                    
        i = lines-1
        j = 0
        while l != "End":                                        
            for line in f:
                l = line  
                i-=1                 
                print(l)
                l = l.split()
                print(l)
                     
                while j < columns:
                    case_ij = lab.laby[i][j]
                    if 'N' not in l[j]:
                        case_ij.North = False
                    elif 'S' not in l[j]:
                        case_ij.South = False
                    elif 'E' not in l[j]:
                        case_ij.Est = False
                    elif 'W' not in l[j]:
                        case_ij.West = False

                    if 'I' in l[j]: #In
                        case_ij.IsEntrence = True
                    elif 'O' in l[j]: #Out
                        case_ij.IsExit = True
                    j +=1
    return lab

                   
f = 'C:\Etude\Projet_info\Projet_Info\Projet_info\Labyrinth.txt'
Lab = readlab(f)
print(Lab)
Lab.show_laby()

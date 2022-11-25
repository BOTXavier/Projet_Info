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

    def __repr__(self):
        self.repr = (self.Nord,self.South,self.Est,self.West)



class labyrinthe:
    def __init__(self,a,b):
        self.lines = a
        self.columns = b
        self.lab = [[Case() for i in range(self.columns)] for j in range[self.lines]]

Lab = labyrinthe(10,10)


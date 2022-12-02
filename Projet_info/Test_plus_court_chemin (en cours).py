def voisin(M,i,j):
    a,b=(len(M[0]),len(M))
    VP= [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
    L=[]
    for k in VP:
        if 0<=k[0]<a and 0<=k[1]<b :
           L.append(k) 
    return L

class Case:
    def  __init__(self):
        #self.x = x
        #self.y = y  
        self.Nord = False
        self.South = False
        self.Est = False
        self.West = False       
        self.IsEntrence = False
        self.IsExit = False
        self.cote=[self.Nord,self.South,self.Est,self.West]

    def __repr__(self):
        return str(self.cote)

class labyrinthe:
    def __init__(self,lines,columns):
        self.lines = lines 
        self.columns = columns
        self.lab = [[Case() for i in range(self.columns)] for j in range(self.lines)]
    def __repr__(self):
        L=self.lab
        n = self.lines 
        p= self.columns
        Laby=[[ [L[i][j].Nord, L[i][j].South] for j in range(p)] for i in range(n)]  # matrice représentant le labyrinthe, le coeff au coodonnée (i,j) contient les informations sur la precence de mur autour de la cellule (de meme coordonnees)  
        return str(Laby)  
 
        
    "methode de construction du laby (methode DFS)"
    def laby_DFS(self): 
        """
        Entree: objet labyrinthe sans chemins (False partout)
        Sortie: objet labyrinthe (construit)
        """     
        p=self.columns
        n=self.lines
        case_traitees=[[False for i in range(p)] for j in range(n)] #permet de marquer True sur les cellules non traitées
        Table_voisins =[[voisin(case_traitees,i,j) for i in range(p)] for j in range(n)]
        def laby_DFS_rec(c):

            k,l=c[0],c[1]
            case_traitees[k][l]= True
            for voisin in Table_voisins[k][l]:
                
                i,j=voisin[0],voisin[1]
                
                if not case_traitees[i][j]: 
                    a,b = self.lab[k][l],self.lab[i][j]
                    
                    if k==i and j>l:     a.Est = b.West = True
                    elif k==i and  j<l:  a.West = b.Est = True 
                    elif j==l and i>k:   a.Nord = b.South = True
                    else :               a.South = b.Nord = True 
                    print(self.lab[k][l])
                    print(case_traitees)
                    laby_DFS_rec(voisin)
                    
        return laby_DFS_rec((0,0))

    

Mon_lab=labyrinthe(3,4)

L=Mon_lab.laby_DFS
print(repr(L))
                

                    

                        












        
        






   

        

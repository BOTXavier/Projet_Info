import Laby_generator_wgrah as lg
from matplotlib import pyplot as plt 
import wgraph as g

def plot_laby(G,t, lab=False):
    """
    Prend en argument un graph G de dictionnaire t, et l'affiche de manière visuelle
    """
    f = G.size()
    n = int((f)**(0.5))
    N = [[i+n*j  for i in range(1,1+n)] for j in range(n) ]
    d = 0.5
    plt.axis([-1, n, -1, n])
    for x in range(n + 1):
        plt.plot((x - d, x - d), (-d, n- d), 'b')
    for y in range(n + 1):
        plt.plot((-d, n - d), (y - d, y - d), 'b')
    for elt in t:
        h = t[elt]
        for h1 in h:
            i = h1//n 
            i1 = elt//n
            try:
                j = N[i].index(h1)
            except: 
                j = N[i-1].index(h1)
                i=i-1
            try: 
                j1 = N[i1].index(elt)
            except:
                j1 = N[i1-1].index(elt)
                i1 = i1-1

            (x,y) = (i1,j1)
            (a,b) = (i,j)
            if a == x + 1: plt.plot((x+d,x+d),(y-d,y+d),'w')
            elif a == x - 1: plt.plot((x-d,x-d),(y-d,y+d),'w')
            elif b == y + 1: plt.plot((x-d,x+d),(y+d,y+d),'w')
            elif y == b + 1: plt.plot((x-d,x+d),(y-d,y-d),'w')
            if lab: plt.plot((x,a), (y,b), 'r')


def plot(n,t,w):
    G = lg.Laby_Graph(n,t,w) 
    g = lg.laby_dict(n,t)
    plot_laby(G,g,lab=False)
    


def plot_soluce(soluce,n): # prend la solution et la taille du côté du laby
    #On transforme les "numéros" en cases (i,j)
    l = []
    i = 0
    j = 0
    for elt in soluce[0]:
        q = elt//n
        r = elt%n
        if r ==0 : 
            i = n-1
            j = q-1
        else : 
            j = q
            i = r-1
        l.append((i,j))

    #On dessine maintenant le lien entre les cases qui sont censées se suivre
    indice = 0
    while indice != soluce[1] : 
        x1 = l[indice][0]
        x2 = l[indice+1][0]
        y1 = l[indice][1]
        y2 = l[indice+1][1]
        plt.plot([y1,y2],[x1,x2],"r")
        indice += 1


    

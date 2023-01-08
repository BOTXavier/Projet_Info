import Laby_generator_wgrah as lg
from matplotlib import pyplot as plt 
import wgraph as g

def plot_laby(G,t, lab=False):
    """
    Prend en argument un graph G de dictionnaire g, et l'affiche de manière visuelle
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
        i = h//n 
        i1 = elt//n
     
        try:
           j = N[i].index(h)
        except: 
            j = N[i-1].index(h)
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
    plt.show()

def plot(n,t,w):
    G = lg.Laby_Graph(n,t,w) 
    g = lg.laby_dict(n,t)
    plot_laby(G,g,lab=False)

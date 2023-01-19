import Laby_generator_wgrah as lg
from matplotlib import pyplot as plt 
from matplotlib.patches import Rectangle
import wgraph as g
from matplotlib.patches import Rectangle


def noeud_en_case(noeud : int, cote : int):
    """
    Converti un noeud en case de coordonnées (i,j)
    """
    i = 0
    j = 0
    q = noeud//cote
    r = noeud%cote
    if r ==0 :  #Si le reste est nul, le noeud est " en haut"
        i = cote-1
        j = q-1
    else : 
        j = q
        i = r-1
    return (i,j)


<<<<<<< HEAD

def graph_to_plot(soluce, n):
    """"
    transforme les "numéros" des noeuds du graphe en une coordonnée (i,j)
    """
    l = []
    i = 0
    j = 0
    for elt in soluce[0]:
        q = elt//n
        r = elt%n
        if r ==0 :  #Si le reste est nul, le noeud est " en haut"
            i = n-1
            j = q-1
        else : 
            j = q
            i = r-1
        l.append((i,j))
    return l 


def plot_laby(G : g.WGraph,t : dict, lab=False):
=======
def plot_laby(G : g.WGraph,t : dict, entrance : int, exit: int, lab=False):
>>>>>>> 7fa6e7a91026b98f2a4b608e5df89292b6d50f3a
    """
    Prend en argument un graph G de dictionnaire t, et l'affiche de manière visuelle
    """
    fig = plt.figure()
    ax = fig.add_subplot()
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
    #colorie l'entrée et la sortie
    x1,y1 = noeud_en_case(entrance,n)
    x1 -= 0.5
    y1-= 0.5
    x2, y2 = noeud_en_case(exit,n)
    x2 -= 0.5
    y2-= 0.5
    rect1 = Rectangle((y1,x1),1,1,color="green")
    rect2 = Rectangle((y2,x2),1,1,color="orange")
    ax.add_patch(rect1)
    ax.add_patch(rect2)


def plot_soluce(soluce : dict,n : int): 
    """
     prend la solution et la taille du côté du laby, et le trace sur un plot
     """
<<<<<<< HEAD
    l = graph_to_plot(soluce,n)
    #On dessine le lien entre les cases qui sont censées se suivre
=======
    #On transforme les "numéros" en cases (i,j)
    l = []
    for elt in soluce[0]:
        l.append(noeud_en_case(elt,n))
    #On dessine maintenant le lien entre les cases qui sont censées se suivre
>>>>>>> 7fa6e7a91026b98f2a4b608e5df89292b6d50f3a
    indice = 0
    while indice != soluce[1] : 
        x1 = l[indice][0]
        x2 = l[indice+1][0]
        y1 = l[indice][1]
        y2 = l[indice+1][1]
        plt.plot([y1,y2],[x1,x2],"r")
        indice += 1


def plot(graph: g.WGraph,dico : dict, soluce : dict, cote : int, title: str, entrance:int, exit:int):
    """
    Plot le labyrinthe et sa solution, avec le titre de la méthode utilisée 
    """
    plot_laby(graph, dico, entrance, exit, lab=False)
    plot_soluce(soluce,cote)
    plt.title(str(title))


<<<<<<< HEAD

=======
>>>>>>> 7fa6e7a91026b98f2a4b608e5df89292b6d50f3a
def coloriage(visite, n):
    """
    colorie les cases visitées 
    """
    l = graph_to_plot(visite, n)
    fig = plt.figure()
    for elt in l:
        ax = fig.add_subplot()
        w = 0.5
        h = 0.5
        rect = Rectangle(elt, w, h, color='gray')
        ax.add_patch(rect)


    

import wgraph 
import random 


def Laby_first_form(n : int): # en entrée 1<=n<=31 
    """ 
    return un graph de n*n noeuds 
    """

    G = wgraph.WGraph() 
    for i in range(1,(n**2)+1):
        G.add_node(i)
    for i in range(1,n+1):
       for j in range(0,(n-1)**2,n):
            G.add_edge(i+j,i+j+n,1)   
    for i in range(1,n):
       for j in range(0,n**2,n):
            G.add_edge(i+j,i+j+1,1) 
    return G 
  

def laby_dict(n : int,t=1): #  1<=n<=31 ; t=1 --> random graph ; t=0 --> graph fixe 
    """
    return un dictionnaire permettant de connaitre le chemin suivi par le dfs. (Laby à n*n noeuds)
    """
    G = Laby_first_form(n)
    nodes = G.nodes()
    Total_sommet = len(nodes)
    deja_visite = {noeud:False for noeud in nodes}
    visite = {"total_sommet_visitée":0 }
    Gf = {}
    depart = nodes[0]
    def dfs_rec(sommet,Gf={}):
        if visite["total_sommet_visitée"] == Total_sommet:
            return Gf
        else : 
            deja_visite[sommet]=True
            visite["total_sommet_visitée"]+=1
            for v in G.voisin(sommet,t):
                if not deja_visite[v]:
                        Gf[v] = sommet
                        dfs_rec(v,Gf)
        return Gf
    Dico= dfs_rec(depart,Gf)
    for item in Dico :                #transforme les valeurs du dico en tableau
        Dico[item]=[Dico[item]]
    Dico[4].append(3) 
    return Dico


def Laby_Graph(g_dict : dict, w=1): # w=1 -> poids 1 sur tous les arretes ; w=0 ->poids random sur arrete(entre 1 et 4)
    ''' 
     return le graph associé au labyrinthe, possédant n*n noeuds 
    '''

    D = g_dict
    G_graph = wgraph.WGraph()
    l = len(D)
    for i in range(1,l+1):
        G_graph.add_node(i)
    if w==1:
        for elt in D:
             G_graph.add_edge(elt,D[elt][0],1)#ne prends que le premier element de la liste ici, a changer peut etre
        return G_graph
    else:
        for elt in D:
             G_graph.add_edge(elt,D[elt][0],random.randint(1,4))
        return G_graph

#ATTENTION ne modifie pas laby dict, juste le graph
#Le Laby généré précédemment est parfait(=0 cycle), algo choisit un sommet aléatoirement, teste si il lui reste des sommets disponibles puis ajoute le sommet
#si carré 1,2,3  4,5,6  7,8,9 alors les voisins geographiques de 2 sont 1,3,5
def Add_Cycles(n,labyGraph,labyDict,nbCycles):
    compt,listeVoisinsGraph=0,[]
    while compt<nbCycles:                                           #répète l'opération m fois pour m cycles
        nbrandom=random.randint(1,n**2)                             #choisit aléatoirement le sommet sur lequel on veut ajouter une arète
        condi=False
        if len(labyGraph.neighbours(nbrandom))< CoinBordOuCentreLaby(n,nbrandom): #regarde si le sommet à moins de voisinsgraph que de voisins possibles(2 pour coin...)
            for item in labyGraph.neighbours(nbrandom):                  #crée la liste des voisins du sommet
                listeVoisinsGraph.append(item[0])
            voisinGeog=voisinGeo(nbrandom,n)
            while condi==False:
                random.shuffle(voisinGeog) 
                if voisinGeog[0] not in listeVoisinsGraph :         #crée un voisin graph si le voisin géographique n'est pas déja dans la liste des voisins graph du sommet
                    labyGraph.add_edge(nbrandom,voisinGeog[0],1)
                    try:
                        labyDict[nbrandom].append(voisinGeog[0])
                    except:
                        labyDict[voisinGeog[0]].append(nbrandom)

                    condi=True
            compt+=1
        listeVoisinsGraph=[]

def voisinGeo(nbrandom:int,n:int):
    """
    calcule les 2 à 4 différents voisins géographiques possibles
    """
    if (nbrandom==1) : return [2,n+1]                               #4 coins
    if (nbrandom==n) : return [n-1,2*n]
    if (nbrandom==n**2-n+1) : return [n**2-2*n+1,n**2-n+2]
    if (nbrandom==n**2) : return [n**2-n,n**2-1]

    if (1<nbrandom<n) : return [nbrandom-1,nbrandom+1,nbrandom+n]   #4 bords
    if (n**2-n+1<nbrandom<n**2) : return [nbrandom-1,nbrandom+1,nbrandom-n]
    if (nbrandom%n==1) : return [nbrandom-n,nbrandom+1,nbrandom+n]
    if (nbrandom%n==0) : return [nbrandom-n,nbrandom-1,nbrandom+n]

    return [nbrandom-n,nbrandom-1,nbrandom+1,nbrandom+n]            #centre


        
def CoinBordOuCentreLaby(n:int,nbrandom:int):#prends un peu de mémoire mais gagne du temps
    if (nbrandom==1 or nbrandom==n or nbrandom==n**2-n+1 or nbrandom==n**2): return 2
    if (nbrandom%n==1 or nbrandom%n==0 or 1<nbrandom<n or n**2-n+1<nbrandom<n**2): return 3
    return 4


def Laby_DictLaby_Graph(n : int,t: int, nbCycles : int, w = 1 ):  
    """
    renvoie un graph et son dictionnaire formant le labyrinthe
    """
    labyDict=laby_dict(n,t)
    labyGraph=Laby_Graph(labyDict,w)
    Add_Cycles(n,labyGraph,labyDict,nbCycles)
    return labyDict,labyGraph


def entrance_exit(cote :int):
    n = cote ** 2
    list1 = [i for i in range(1,cote+1)]
    list3 = [ i for i in range(n - cote+1,n+1)]
    list = [(1 + i * cote) for i in range(1,cote-1)]
    list2 = [(i * cote) for i in range(2,cote)]   
    l = list + list2 + list3 + list1
    l.sort()
    random.shuffle(l)
    return l[0],l[1]

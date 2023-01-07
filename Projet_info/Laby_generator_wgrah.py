import wgraph 
import random 

def Laby_first_form(n): # en entrée 1<=n<=31 
    """ return un graph de n*n noeuds """

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
  

def laby_dict(n,t): #  1<=n<=31 ; t=1 --> random graph ; t=0 --> graph fixe 
    """return un dictionnaire permettant de connaitre le chemin suivi par le dfs. (Laby à n*n noeuds)"""
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
    return dfs_rec(depart,Gf)


def Laby_Graph(n,t,w):  # 1<=n<=31 ; t=1 -> random graph ; t=0 -> graph fixe ; w=1 -> poids 1 sur tous les arretes ; w=0 ->poids random sur arrete(entre 1 et 4)
    '''  return le graph associé au labyrinthe, possédant n*n noeuds 
    '''
    D = laby_dict(n,t)
    G = wgraph.WGraph()
    l = len(D)
    for i in range(1,l+1):
        G.add_node(i)
    if w==1:
        for elt in D:
             G.add_edge(elt,D[elt],1)
        return G
    else:
        for elt in D:
             G.add_edge(elt,D[elt],random.randint(1,4))
        return G
    
#def Laby_wgraph(n,t):














    







import wgraph 
import random 
from math import sqrt 



def Laby_first_form(n): # en entrée un carré parfait n tel que 1<=n<=961 (pour un soucis ultérieur de représentation )

    
   
    G = wgraph.WGraph() # on pouvait ici utliser le module graph(sans les poids) car pour l'instant ce sont les chemins qui nous interessent
    for i in range(1,n+1):
        G.add_node(i)
    n_rac = int(sqrt(n))
    for i in range(1,n_rac+1):
       for j in range(0,(n_rac-1)**2,n_rac):
            G.add_edge(i+j,i+j+n_rac,random.randint(1,5))   
    for i in range(1,n_rac):
       for j in range(0,n,n_rac):
            G.add_edge(i+j,i+j+1,random.randint(1,5)) 
    return G 
  

def laby_dict(G,t): # t=1 --> random graph ; t=0 --> graph fixe
    '''
    permet de constuire le labyrinthe en parcourant tous les noeuds avec l'algo de base du dfs , 
    fonction retournant le graphe sous forme dictionnaire qui indique quel noeud est maintenant branché (ou lié) à quel noeud,
    En gros , on construit les chemins possibles !
    '''

    nodes = G.nodes()
    Total_sommet = len(nodes)
    deja_visite = {noeud:False for noeud in nodes}
    visite = {"total_sommet_actuelle":0 }
    Gf = {}    # c'est le dictionnaire décrit dans le commentaire précédent
    depart = nodes[0]
    
    def dfs_rec(sommet,Gf={}):
        if visite["total_sommet_actuelle"] == Total_sommet:
            return Gf
        else : 
            deja_visite[sommet]=True
            visite["total_sommet_actuelle"]+=1
            for v in G.voisin(sommet,t):
                if not deja_visite[v]:
                        Gf[v] = sommet
                        dfs_rec(v,Gf)
        return Gf
    return dfs_rec(depart,Gf)


def Laby_Graph(D):   
    '''  
    permet de convertir le laby en dictionnaire (fourni par la fonction Laby_dict ) 
    en Laby sous forme de Graphe (Final form!)
    '''
    G = wgraph.WGraph()
    L = D.keys()
    for i in range(1,len(L)+1):
        G.add_node(i)
    for elt in D:
        G.add_edge(elt,D[elt],random.randint(1,4))
    return G




   

   

if __name__=="__main__":

    G = Laby_first_form(25)
    r = laby_dict(G,t=1)
    LG=Laby_Graph(r)

    print(G)
    print(r)
    print(LG)




    







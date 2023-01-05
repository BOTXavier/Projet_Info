import wgraph 
import random 
from math import sqrt 



def Laby_fisrt_form(n): # en entrée un carré parfait n tel que 1<=n<=961 (pour un soucis ultérieur de représentation )

    ''' permet de générer n*n noeuds et et de les reliés chacun avec leur voisin tel une matrice,
     les noeuds sont numérotés de 1 à n*n, L'obejectif était de construire d'abord un graphe connexe et "ultra" cyclique '''
   
    G = wgraph.WGraph() # on pouvait ici utlisé le module graph(sans les poids) car pour l'instant ce sont les chemins qui nous interessent
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

    

def laby_dict(G): # en entrée un Graphe fourni par Laby_first_form()
    
    '''permet de constuire le labyrinthe en parcourant tous les noeuds avec l'algo de base du dfs , 
    fonction retournant le graphe sous forme dictionnaire qui indique quel noeud est maintenant branché (ou lié) à quel noeud,
    En gros , on construit les chemins possibles !'''

    nodes = G.nodes()
    Total_sommet = len(nodes)
    deja_visiter = {noeud:False for noeud in nodes}
    visite = {"total_sommet_actuelle":0 }
    Gf = {}    # c'est le dictionnaire décrit dans le commentaire précédent
    depart = nodes[0]
    
    def dfs_rec(sommet,Gf={}):
        if visite["total_sommet_actuelle"] == Total_sommet:
            return Gf
        else : 
            deja_visiter[sommet]=True
            visite["total_sommet_actuelle"]+=1
            L=[]
            for v in G.neighbours(sommet):
                voisin = v[0]
                L.append(voisin)
            random.shuffle(L)    # cette astuce du shuffle est le coeur de l'algo (cela permet de choisir les voisins aléatoirement), sinon dfs allait betement suivre un chemin tout droit 
            for voisin in L:
                if not deja_visiter[voisin]:
                        Gf[voisin] = sommet
                        dfs_rec(voisin,Gf)
        return Gf
    return dfs_rec(depart,Gf)

def Laby_Graph(D):   
    '''permet de convertir le laby en dictionnaire (fourni par la fonction Laby_dict ) 
    en Laby sous forme de Graphe (Final form!)'''
    G = wgraph.WGraph()
    L = D.keys()
    for i in range(1,len(L)+1):
        G.add_node(i)
    for elt in D:
        G.add_edge(elt,D[elt],random.randint(1,4))
    return G




   

   

if __name__=="__main__":

    G = Laby_fisrt_form(25)
    r = laby_dict(G)
    LG=Laby_Graph(r)

    print(G)
    print(r)
    print(LG)




    







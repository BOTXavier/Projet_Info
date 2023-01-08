import Laby_generator_wgrah as lg
import prioqueue as pq


inf=10000

def initialisation(G,start):
    L = G.nodes()
    d = {}
    for u in L:
        d[u]=inf
    d[start]=0
    
    return d

def find_min(Q):
    a=Q
    b = a.pop()
    return b[1]

def maj_dist(s1,s2,predecesseur,d,G):
    a = G.weight(s1,s2)
    
    if d[s2] > d[s1] + a :
        d[s2] = d[s1] + a
        predecesseur[s2] = s1

    return d,predecesseur


def dijkstra_classic(G,start,end):
    """return le chemin le plus court (liste de noeuds successif) et la longueur de ce chemin"""
    
    d = initialisation(G,start)
    L = G.nodes()
    Lq = [(d[u],u) for u in L]
    Q = pq.PrioQueue(Lq)
    
    predecesseur ={}

    while not Q.is_empty():
        u = find_min(Q)
        for v in G.neighbours(u):
            maj_dist(u,v[0],predecesseur,d,G)
            Q.decrease_prio(v[0],d[v[0]])
    A = []
    s = end
    while s!=start : 
        A =[s]+A
        s = predecesseur[s]
    A = [start] + A
    return A,d[end]

G=lg.Laby_Graph(5,0,1)
#print(G)

r=dijkstra_classic(G,1,887)
print(f'le chemin le plus court est {r}')




  
    












    












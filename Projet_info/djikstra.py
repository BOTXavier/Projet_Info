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
    a = Q.pop()
    return a[1]

def maj_dist(s1,s2,d,G):
    a = G.weight(s1,s2)
    
    if d[s2] > d[s1] + a :
        d[s2] = d[s1] + a
        
    return d


def dijkstra_classic(G,start,end):
    
    d = initialisation(G,start)
    
    L = G.nodes()
    Lq = [(d[u],u) for u in L]
    Q = pq.PrioQueue(Lq)
    predecesseur ={}

    while not Q.is_empty():
        u = find_min(Q)
        Q.pop()
        
        for v in G.neighbours(u):
            maj_dist(u,v[0],d,G)
            predecesseur[v[0]] = u
            Q.decrease_prio(v[0],d[v[0]])
    print(predecesseur)
    A = []
    s = end
    while s!=start : 
        A =[s]+A
        s = predecesseur[s]
    A = [start] + A
    return A,d[end]









  
    












    












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




  

def dijkstra_bidirect(G,start,end):
    """return le chemin le plus court (liste de noeuds successif) et la longueur de ce chemin"""
    best_dist = 100000 # initialiser à l'infini 
    d1 = initialisation(G,start)
    d2 = initialisation(G,end)
    
    L = G.nodes()
    Lq = [(d1[u],u) for u in L]
    
    Lq2= [(d2[u],u) for u in L]
    Q1 = pq.PrioQueue(Lq)
    Q2 = pq.PrioQueue(Lq2)
    predecesseur1 ={}
    predecesseur2 ={}
    S1 = []
    S2 = []
    while not (Q1.is_empty() or Q2.is_empty()):
        u1, u2 = find_min(Q1) , find_min(Q2)
        
        S1.append(u1)
        S2.append(u2)
        for v in G.neighbours(u1):
            maj_dist(u1,v[0],predecesseur1,d1,G)
            Q1.decrease_prio(v[0],d1[v[0]])
            if v[0] in S1 and d1[u1] + G.weight(u1,v[0]) + d2[v[0]] < best_dist:
                best_dist = d1[u1] + G.weight(u1,v[0]) + d2[v[0]] 
                print(best_dist)
        
        for v in G.neighbours(u2):
            maj_dist(u2,v[0],predecesseur2,d2,G)
            Q2.decrease_prio(v[0],d2[v[0]])
            if v[0] in S2 and d2[u2] + G.weight(u2,v[0]) + d1[v[0]] < best_dist:
                best_dist = d2[u2] + G.weight(u2,v[0]) + d1[v[0]] 
                print(best_dist)
        
        if d1[u1]+d2[u2] >= best_dist : break
    
    A = []
    B = []
    s = u1
    while s!=start : 
        A =[s]+A
        s = predecesseur1[s]
    A = [start] + A
    
    B = []
    s2 = u2 
    while s2!=end : 
        B = B + [s2]
        s2 = predecesseur2[s2]
    B = B + [end]
    print(A,B)
    
    return A+B, best_dist


                        
                     
                     
                     
       








    












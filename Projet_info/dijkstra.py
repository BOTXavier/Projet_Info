import Laby_generator_wgrah as lg
import prioqueue as pq
import time 

INF = 10000

def initialisation(G,start: int):
    L = G.nodes()
    d = {}
    for u in L:
        d[u]= INF
    d[start]=0
    
    return d

def find_min(Q : pq.PrioQueue):
    a=Q
    b = a.pop()
    return b[1]

def maj_dist(s1:int, s2:int, predecesseur : dict, d :dict , G):
    a = G.weight(s1,s2)
    
    if d[s2] > d[s1] + a :
        d[s2] = d[s1] + a
        predecesseur[s2] = s1

    return d,predecesseur


def dijkstra_classic(G,start : int , end: int):  #G un graphe
    """
    return le chemin le plus court (liste de noeuds successif) et la longueur de ce chemin
    """
    time_begin = time.time()
    d = initialisation(G,start)
    L = G.nodes()
    Lq = [(d[u],u) for u in L]
    Q = pq.PrioQueue(Lq)
    
    predecesseur ={}
    visite = []
    while not Q.is_empty():
        u = find_min(Q)
        visite.append(u)
        for v in G.neighbours(u):
            maj_dist(u,v[0],predecesseur,d,G)
            Q.decrease_prio(v[0],d[v[0]])
    A = []
    s = end
    while s!=start : 
        A +=[s]
        s = predecesseur[s]
    A += [start]
    time_end = time.time()
    execution_time = time_end - time_begin 
    return A,d[end],visite, execution_time




  

def dijkstra_bidirect(G,start : int, end : int):#G un graphe
    """
    return le chemin le plus court (liste de noeuds successif) et la longueur de ce chemin
    """
    time_begin = time.time()
    best_dist = 100000 # initialiser à l'infini 
    d1 = initialisation(G,start)
    d2 = initialisation(G,end)
    
    L = G.nodes()
    Lq = [(d1[u],u) for u in L]
    Lq2= [(d2[u],u) for u in L]
    Q1 = pq.PrioQueue(Lq)
    Q2 = pq.PrioQueue(Lq2)
    predecesseur1,predecesseur2  = {},{}
    S1 ,S2 = [] ,[]
    h1,h2= [best_dist,start],[best_dist, end]
    h=0
    while not (Q1.is_empty() or Q2.is_empty()):
        u1, u2 = find_min(Q1) , find_min(Q2)
        S1.append(u1)
        S2.append(u2)
        
        for v in G.neighbours(u1):
            
            maj_dist(u1,v[0],predecesseur1,d1,G)
            
            Q1.decrease_prio(v[0],d1[v[0]])
            if v[0] in S2 and d1[u1] + G.weight(u1,v[0]) + d2[v[0]] < best_dist:
                best_dist = d1[u1] + G.weight(u1,v[0]) + d2[v[0]]
         
              
        
        for v in G.neighbours(u2):
            maj_dist(u2,v[0],predecesseur2,d2,G)
            Q2.decrease_prio(v[0],d2[v[0]])
            
            if v[0] in S1 and d2[u2] + G.weight(u2,v[0]) + d1[v[0]] < best_dist:
                best_dist = d2[u2] + G.weight(u2,v[0]) + d1[v[0]]

        if u1 in S2:
            h1[0],h1[1] = best_dist,u1
            print(h1)
        elif u2 in S1:
            h2[0],h2[1] = best_dist,u2
            print(h2)
            
        elif d1[u1]+d2[u2] >= best_dist :
          break
    
    if h1[0]>h2[0]: h=h2[1]
    else : h=h1[0]
    print(h,predecesseur1,predecesseur2)
    A = []
    B = []
    s = h
    while s!=start : 
        A =[s]+A
        s = predecesseur1[h]
        
    A = [start]+A
    
    B = []
    s2 = predecesseur2[h]
    while s2!=end : 
        B += [s2]
        s2 = predecesseur2[s2]
    B += [end]
    print(A,B)
    time_end = time.time()
    execution_time = time_end - time_begin 
    return A+B, best_dist, execution_time


                        
                     
                     
                     
       








    












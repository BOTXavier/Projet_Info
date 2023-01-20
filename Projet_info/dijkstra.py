import Laby_generator_wgrah as lg
import prioqueue as pq
import time 


def initialisation(G,start: int):
    INF = 10000
    L = G.nodes()
    dist = {}
    for u in L:
        dist[u]= INF
    dist[start]=0
    return dist

def find_min(heap_node : pq.PrioQueue):
    b = heap_node.pop()
    return b[1]

def maj_dist(s1:int, s2:int, predecesseur : dict, dist :dict , Graph):
    a = Graph.weight(s1,s2)
    
    if dist[s2] > dist[s1] + a :
        dist[s2] = dist[s1] + a
        predecesseur[s2] = s1
    return dist,predecesseur
def delete_double(L):
    new_list = [] 
    for i in L : 
        if i not in new_list: 
            new_list.append(i) 
    return new_list





def dijkstra_classic(G,start : int , end: int):  #G un graphe
    """
    return le chemin le plus court (liste de noeuds successif) et la longueur de ce chemin
    """
    time_begin = time.time()
    dist = initialisation(G,start)
    L = G.nodes()
    Lq = [(dist[u],u) for u in L]
    forward_heap = pq.PrioQueue(Lq)
    
    predecesseur ={}
    visite = []
    while not forward_heap.is_empty():
        node = find_min(forward_heap)
        visite.append(node)
        for voisin,poids in G.neighbours(node):
            maj_dist(node,voisin,predecesseur,dist,G)
            forward_heap.decrease_prio(voisin,dist[voisin])
    A = []
    s = end
    while s!=start : 
        A +=[s]
        s = predecesseur[s]
    A += [start]
    time_end = time.time()
    execution_time = time_end - time_begin 
    return A,dist[end],visite, execution_time


def dijkstra_bidirect(G,start : int, end : int): #G un graphe
    time_begin = time.time()
    d1 = initialisation(G,start)
    d2 = initialisation(G,end)
    L = G.nodes()
    Lq = [(d1[u],u) for u in L]
    Lq1= [(d2[u],u) for u in L]
    forward_heap = pq.PrioQueue(Lq)
    backward_heap = pq.PrioQueue(Lq1)
    forward_visited , backward_visited = [] , []
    forward_path = {start: []}
    backward_path = {end: []}
    
    while not (forward_heap.is_empty() or backward_heap.is_empty()):
        # Get the node with the smallest distance from the forward heap
        node_f = find_min(forward_heap)
        forward_dist, forward_node = d1[node_f] , node_f 
        # If the node has not been visited 
        if forward_node not in forward_visited:
            # Mark it as visited
            forward_visited.append(forward_node)
            # If the node is also in the backward visited set, we have found the shortest path
            if forward_node in backward_visited:
                back_path = delete_double(backward_path[forward_node][::-1])
                time_end = time.time()
                execution_time = time_end - time_begin 
                print(forward_path[forward_node], backward_path[forward_node][::-1])
                return forward_path[forward_node] + back_path , forward_dist + d2[forward_node],execution_time
            # If not, update the distances and paths of its neighbors and add them to the heap
            for voisin,poids in G.neighbours(forward_node):
                if voisin not in forward_visited:
                    new_dist = forward_dist + poids 
                    if new_dist < d1[voisin]:
                        d1[voisin] = new_dist
                        forward_path[voisin] = forward_path[forward_node] + [forward_node]
                        forward_heap.decrease_prio(voisin,new_dist)
        # Do the same thing for the backward heap
        node_b = find_min(backward_heap)
        backward_dist, backward_node = d2[node_b] , node_b 
        if backward_node not in backward_visited:
            backward_visited.append(backward_node)
            if backward_node in forward_visited:
                backward_path[backward_node].reverse()
                back_path = delete_double(backward_path[backward_node])
                time_end = time.time()
                execution_time = time_end - time_begin 
                print (forward_path[backward_node], backward_path[backward_node],"b")
                return forward_path[backward_node] + back_path ,backward_dist + d1[backward_node],execution_time
            for voisin,poids in G.neighbours(backward_node):
                if voisin not in backward_visited:
                    new_dist = backward_dist + poids 
                    if new_dist < d2[voisin]:
                        d2[voisin] = new_dist
                        backward_path[voisin] = backward_path[backward_node]+[backward_node]+[voisin]
                        backward_heap.decrease_prio(voisin,new_dist)
    time_end = time.time()
    execution_time = time_end - time_begin 
    return "absence de plus court chemin !!! vérifier si vous avez mis le bon start et end",execution_time
                              
         
        

        


    






                     
                     
       








    












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
        if node == end : break
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
    return A,dist[end], execution_time, visite 


def dijkstra_bidirect(Graph ,start : int, end : int): 
    dist1 = initialisation(Graph,start)
    dist2 = initialisation(Graph,end)
    L = Graph.nodes()
    Lq = [(dist1[u],u) for u in L]
    Lq1= [(dist2[u],u) for u in L]
    forward_heap = pq.PrioQueue(Lq)
    backward_heap = pq.PrioQueue(Lq1)
    forward_visited , backward_visited = [] , []
    forward_path, backward_path =  {start: []}, {end: []}
    time_begin = time.time()
    while not (forward_heap.is_empty() or backward_heap.is_empty()):
        # récupèrer le noeud avec la plus petite distance
        node_f = find_min(forward_heap)
        forward_dist, forward_node = dist1[node_f] , node_f 
        # si ce noeud n'a pas été visité
        if forward_node not in forward_visited:
            # Le marquer comme visité
            forward_visited.append(forward_node)
            # si le noeud est present dans le backward_visisited, chemin trouvé , fin de l'algo
            if forward_node in backward_visited:
                back_path = delete_double(backward_path[forward_node][::-1])
                time_end = time.time()
                execution_time = time_end - time_begin 
                return forward_path[forward_node] + back_path , forward_dist + dist2[forward_node],execution_time, forward_visited, backward_visited
            # sinon, mise a jour du poids de chaque noeud voisin 
            for voisin,poids in Graph.neighbours(forward_node):
                if voisin not in forward_visited:
                    new_dist = forward_dist + poids 
                    if new_dist < dist1[voisin]:
                        dist1[voisin] = new_dist
                        forward_path[voisin] = forward_path[forward_node] + [forward_node]
                        forward_heap.decrease_prio(voisin,new_dist)
        # Faire la meme chose de l'autre zone de recherche (backward_search)
        node_b = find_min(backward_heap)
        backward_dist, backward_node = dist2[node_b] , node_b 
        if backward_node not in backward_visited:
            backward_visited.append(backward_node)
            if backward_node in forward_visited:
                backward_path[backward_node].reverse()
                back_path = delete_double(backward_path[backward_node])
                time_end = time.time()
                execution_time = time_end - time_begin 
                return forward_path[backward_node] + back_path, backward_dist + dist1[backward_node], execution_time, forward_visited, backward_visited
            for voisin,poids in Graph.neighbours(backward_node):
                if voisin not in backward_visited:
                    new_dist = backward_dist + poids 
                    if new_dist < dist2[voisin]:
                        dist2[voisin] = new_dist
                        backward_path[voisin] = backward_path[backward_node]+[backward_node]+[voisin]
                        backward_heap.decrease_prio(voisin,new_dist)
    time_end = time.time()
    execution_time = time_end - time_begin 
    return "absence de plus court chemin !!! vérifier si vous avez mis le bon start et end",execution_time
                              
import random
import heapq

class WGraph(object):
    
    def __init__(self):
        """Initialize an empty weighted graph"""
        self.adj = {}


    def __repr__(self):
        """String representation"""
        return '<WGraph: {0.adj}>'.format(self)


    def add_node(self, u : int):
        """
        Add node u to the graph
        u must be of an orderable type (int for example)
        """
        self.adj[u] = []


    def add_edge(self, u : int, v : int , weight : int):
        """
        Add edge (u, v, weight) to the graph,
        and the nodes u et v if necessary
        """
        self.adj.setdefault(u, []).append((v, weight))
        self.adj.setdefault(v, []).append((u, weight))


    def size(self):
        """Return the number of nodes in the graph"""
        return len(self.adj)


    def nodes(self):
        """Return the list of nodes in the graph"""
        return [u for u in self.adj]


    def edges(self):
        """Return the list of edges (u, v, weight) of the graph"""
        return [(u, v, weight)
                for u in self.adj for (v, weight) in self.adj[u] if u < v]
    

    def neighbours(self, u : int):
        """Return the list of neighbours (v, weight) of node u in the graph"""
        return self.adj[u]
    

    def weight(self,u : int, v : int):
        """return weight u-v"""
        w=0
        for a in self.adj[u]:
            if v==a[0]: 
                w=a[1]
        
        return w
        

    def voisin(self,u : int, t : int):
        """return the list of neighbours v (type int) of node u in the graph """ 
        L=[]
        for voisin in self.neighbours(u):
            L.append(voisin[0])
        if t==0 :
            heapq.heapify(L)
            return L
        elif t==1:
            random.shuffle(L)
            return L
    

class laby(object):
    def __init__(self,G : WGraph,g : dict,n : int ,m : int):
        self.Graph = G
        self.dico = g
        self.cote = n
        self.cycle = m

        
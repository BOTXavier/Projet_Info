import random

class WGraph(object):
    
    def __init__(self):
        """Initialize an empty weighted graph"""
        self.adj = {}

    def __repr__(self):
        """String representation"""
        return '<WGraph: {0.adj}>'.format(self)

    def add_node(self, u):
        """
        Add node u to the graph
        u must be of an orderable type (int for example)
        """
        self.adj[u] = []

    def add_edge(self, u, v, weight):
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
    
    def neighbours(self, u):
        """Return the list of neighbours (v, weight) of node u in the graph"""
        return self.adj[u]

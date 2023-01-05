class Graph(object):
    
    def __init__(self):
        """Cree un graphe vide"""
        self.adj = {}

    def __repr__(self):
        """Representation en chaine de caracteres d'un graphe"""
        return '<Graph: {0.adj}>'.format(self)

    def add_node(self, u):
        """Ajoute un noeud u au graphe"""
        self.adj[u] = []

    def add_edge(self, u, v):
        """Ajoute l'arete (u, v) au graphe"""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def size(self):
        """Renvoie le nombre de noeuds du graphe"""
        return len(self.adj)         

    def nodes(self):  
        """Renvoie la liste des noeuds du graphe"""
        return self.adj.keys()

    def neighbours(self, u):
        """Renvoie la liste des voisins du noeud u dans le graphe"""
        return self.adj[u]

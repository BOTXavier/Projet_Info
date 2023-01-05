class Node:

    def __init__(self, id):
        self.adj = {}
        self.id = id
    
    def __repr__(self):
        return str(self.adj)

    def add(self, v, w):
        self.adj[v] = w
    
    def remove(self, v):
        self.adj.pop(v)

    def is_adj(self, v):
        return v in self.adj
    
    def weight(self, v):
        return self.adj[v]
    
    def neighbours(self, v):
        return self.adj.items()

    def __lt__(self, other):
        return self.dist < other.dist


class WGraph:


    def __init__(self):
        self.nodes = {}
    
    def __repr__(self) -> str:
        return str(self.nodes)

    def add_node(self, u):
        self.nodes[u] = Node(u)
    
    def get_node(self, u):
        return self.nodes[u]
    
    def is_node_in(self, u):
        return u in self.nodes

    def add_edge(self, u, v, w):
        unode = self.nodes.setdefault(u, Node(u))
        if not (unode.is_adj(v)): unode.add(v, w)
        vnode = self.nodes.setdefault(v, Node(v))
        if not (vnode.is_adj(u)): vnode.add(u, w)
    
    def remove_edge(self, u, v):
        self.nodes[u].remove(v)
        self.nodes[v].remove(u)

    def weight(self, u, v):
        return self.nodes[u].weight(v)
    
    def neighbour(self, u):
        return self.nodes[u].neighbours()

    def dfs(self, entry, exit):
        for node in self.nodes.values():
            node.explored = False
        def dfs_rec(u):
            print(self.nodes[u].id, end=' ')
            self.nodes[u].explored = True
            if u == exit : return True
            for (v, _) in self.neighbour(u):
                if not self.nodes[v].explored:
                    if dfs_rec(v): return True
            return False
        if not dfs_rec(entry): raise NotFound


                    


    

laby = WGraph()
laby.add_node((0,0))
laby.add_node((1,0))
laby.add_node((3,1))
laby.add_node((1,1))
laby.add_node((2,3))
laby.add_node((2,2))
laby.add_node((1,2))
laby.add_node((3,3))

laby.add_edge((0, 0), (1, 0), 1)
laby.add_edge((1, 0), (1, 1), 1)
laby.add_edge((1, 0), (3, 1), 3)
laby.add_edge((1, 1), (2, 3), 5)
laby.add_edge((1, 1), (2, 2), 2)
laby.add_edge((2, 2), (1, 2), 1)
laby.add_edge((2, 2), (3, 3), 3)
laby.dfs((0,0), (3,3))

# g = WGraph()
# for i in range(6):
#     g.add_node(i)

# g.add_edge(0, 1, 2)
# g.add_edge(0, 3, 1)
# g.add_edge(3, 1, 2)
# g.add_edge(2, 1, 3)
# g.add_edge(3, 2, 3)
# g.add_edge(3, 4, 1)
# g.add_edge(2, 4, 1)
# g.add_edge(2, 5, 5)
# g.add_edge(4, 5, 1)
# print(g)



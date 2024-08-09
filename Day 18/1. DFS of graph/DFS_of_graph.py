class Solution:
    def __init__(self):
        self.dfs = []
        self.visited = set([0])
    def traverse(self, vtx,V,adj):
        self.dfs.append(vtx)
        for v in adj[vtx]:
            if v not in self.visited:
                self.visited.add(v)
                self.traverse(v,V,adj)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        self.traverse(0,V,adj)
        return self.dfs
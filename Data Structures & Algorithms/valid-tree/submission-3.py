class Solution:
    def dfs(self, i: int, parent: int, vis: List[int], adj: List[List[int]]) -> bool:
        vis[i] = 1

        for j in adj[i]:
            if not vis[j]:
                if self.dfs(j, i, vis, adj):
                    return True
            elif j != parent:
                return True

        return False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        vis = [0] * n
        if(self.dfs(0,-1,vis,adj)):
            return False
        for i in range(n):
            if not vis[i]:
                return False
        return True
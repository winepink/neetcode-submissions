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
        if len(edges) != n - 1: 
            return False

        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        vis = set()
        def dfs(node):
            vis.add(node)
            for nei in adj[node]:
                if nei not in vis:
                    dfs(nei)

        dfs(0)

        return len(vis) == n

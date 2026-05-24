class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        cnt=0
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        vis=[0]*n
        def dfs(i):
            nonlocal adj,vis
            vis[i]=1
            for k in adj[i]:
                if vis[k]!=1:
                    dfs(k)
        for i in range(n):
            if vis[i]!=1:
                dfs(i)
                cnt+=1
        return cnt
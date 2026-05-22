class Solution:
    def dfs(self, i: int, vis: List[int], st: List[int], adj: List[List[int]]) -> bool:
        vis[i]=1
        st[i]=1
        for j in adj[i]:
            if(st[j]):
                return True
            if not vis[j] and self.dfs(j,vis,st,adj):
                return True
        st[i]=0
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #loop detection in a directed graph
        adj = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            adj[j].append(i)
        vis = [0] * numCourses
        st = [0] * numCourses
        for i in range(numCourses):
            if not vis[i] and self.dfs(i,vis,st,adj):
                return False
        return True
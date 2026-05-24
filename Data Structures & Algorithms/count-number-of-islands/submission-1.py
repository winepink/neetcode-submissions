class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt=0
        n=len(grid)
        m=len(grid[0])
        vis = [[0] * m for _ in range(n)]
        def dfs(i,j):
            vis[i][j]=1
            for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                ni = i + x
                nj = j + y

                if (
                    0 <= ni < n and
                    0 <= nj < m and
                    grid[ni][nj] == "1" and
                    vis[ni][nj] != 1
                ):
                    dfs(ni,nj)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and vis[i][j]!=1:
                    dfs(i,j)
                    cnt+=1
        return cnt
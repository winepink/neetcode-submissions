func countComponents(n int, edges [][]int) int {
    adj := make([][]int, n)

    cnt:=0
    for _,edge := range edges{
        a:=edge[0]
        b:=edge[1]
        adj[a]=append(adj[a],b)
        adj[b]=append(adj[b],a)
    }
    vis := make([]int, n)
    var dfs func(int)
    dfs = func(i int) {
        vis[i]=1
        for _,k := range adj[i]{
            if vis[k]!=1{
                dfs(k)
            }
        }
    }
    for i := 0; i < n; i++ {
        if vis[i]!=1{
            dfs(i)
            cnt+=1
        }
    }
    return cnt
}

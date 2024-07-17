class Solution:
    
    def __init__(self):
        self.ans = []
        self.visited = []

    def DFS(self, adj, curr):
        self.visited[curr] = True
        self.ans.append(curr)
        for neighbor in adj[curr]:
            if not self.visited[neighbor]:
                self.DFS(adj, neighbor)

    def dfsOfGraph(self, V, adj):
        # Initialize visited list and ans list
        self.visited = [False] * V
        self.ans = []

        # Perform DFS starting from node 0
        self.DFS(adj, 0)
        
        return self.ans
    

#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends
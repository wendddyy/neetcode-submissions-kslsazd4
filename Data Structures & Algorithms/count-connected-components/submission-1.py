class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {i :[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        res = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
        

        
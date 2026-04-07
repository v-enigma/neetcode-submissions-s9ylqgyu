class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def dfs(node):
            visited.add(node)
            for node in adjList.get(node,[]):
                if node not in visited:
                    dfs(node)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count = count + 1
        return count


        
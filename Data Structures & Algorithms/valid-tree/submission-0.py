class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        visited = set()
        for i in range(0, n):
            adjList[i] =[]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        def dfs(node ,parent):
            visited.add(node)
            for adj in adjList.get(node, []):
                if adj not in visited:
                    if not dfs(adj , node):
                        return False
                elif adj!= parent:
                    return False
            return True
        isTree = False
        count = 0
        for i in range(n):
            if i not in visited:
                if count == 0:
                    isTree = dfs(i,-1)
                else:
                    isTree = False
                    break
                count = count +1
        
        return isTree and count == 1
                
            
        
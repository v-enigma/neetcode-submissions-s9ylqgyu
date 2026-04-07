class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       adjList  = {}
       visited = {}
       for item in prerequisites:
        if item[0] in  adjList:
            adjList[item[0]].append(item[1])
        else:
            adjList[item[0]] = [item[1]]
       def dfs(index):
        if index in adjList:
            if index in visited:
                if  visited[index] == "InProgress":
                    return False
                if visited[index] == "Visited":
                    visited[index] = "InProgress"

            dependencies = adjList[index]
            visited[index] = "InProgress"
            result = True
            for dep in dependencies:
                result = result and  dfs(dep)
            visited[index] = "visited"
            return result
                    
        else:
            visited[index] = "visited"
            return True
       index = 0
       result = True
       while( index < numCourses ):
        if index not in  visited :
            result = result and dfs(index)
        index= index + 1
       return result 

        
       


        
       
       


            

            



        






        
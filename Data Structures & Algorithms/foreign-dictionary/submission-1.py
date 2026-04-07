class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        visited = set()
        visiting = set()  # for cycle detection
        result = []

        def findOrder(word1, word2):
            k = 0
            while k < len(word1) and k < len(word2):
                if word1[k] != word2[k]:
                    return (word1[k], word2[k])
                k += 1
            if len(word1) > len(word2):
                return "INVALID"
            return (-1, -1)

        def buildGraph():
            for i in range(len(words) - 1):
                order = findOrder(words[i], words[i+1])
                if order == "INVALID":
                    return False
                if order != (-1, -1):
                    a, b = order
                    if a not in adjList:
                        adjList[a] = []
                    adjList[a].append(b)
            return True

        def dfs(node):
            if node in visiting:  # cycle detected
                return False
            if node in visited:
                return True
            visiting.add(node)
            for neighbor in adjList.get(node, []):
                if not dfs(neighbor):
                    return False
            visiting.remove(node)
            visited.add(node)
            result.append(node)
            return True

        if not buildGraph():
            return ""

        all_chars = set(c for word in words for c in word)
        for node in all_chars:
            if not dfs(node):
                return ""

        return "".join(result[::-1])



            

            


        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexMap = {}
        result = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            if temperatures[i] in indexMap:
                indexMap[temperatures[i]].append(i) 
            else:
                indexMap[temperatures[i]] = [i]
        stack = []
        for i in range(len(temperatures)):
            if len(stack) == 0  or stack[-1] >= temperatures[i] :
                stack.append(temperatures[i])
            else:
                while len(stack) > 0 and stack[-1] < temperatures[i]:
                    removed = stack.pop()
                    index  = indexMap[removed].pop(0)
                    print(i,index, removed)
                    result[index] = i - index
                stack.append(temperatures[i])
        return result

            

        


        
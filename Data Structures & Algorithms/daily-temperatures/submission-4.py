class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0]*len(temperatures)
        
        stack = []
        for i in range(len(temperatures)):
            
                while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                    removed = stack.pop()
                    result[removed] = i - removed
                stack.append(i)
        return result

            

        


        
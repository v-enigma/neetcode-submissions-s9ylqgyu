class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)-2, -1,-1):
            count = 0
            for j in range(i+1, len(temperatures)):
                count = count +1
                if temperatures[i] < temperatures[j]:
                    result[i] = count 
                    break
        return result 
            


        
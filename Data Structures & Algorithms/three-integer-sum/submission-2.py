class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        def twoSum(left, target):
            numMap = set()
            solutions = []
            for i in range(left, len(nums)):
                leftOver = target - nums[i]
                if leftOver in numMap:
                    solutions.append([leftOver, nums[i]])
                numMap.add(nums[i])
            return solutions
                
        for i in range(len(nums) - 1):
            for pair in twoSum(i + 1, -nums[i]):
                pair.append(nums[i])
                pair.sort()
                result.add(tuple(pair))
                
        return [list(t) for t in result]
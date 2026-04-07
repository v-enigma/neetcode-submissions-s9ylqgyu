class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i , k in enumerate(nums):
            if k in nums_dict:
                nums_dict[k].append(i)
            else:
                nums_dict[k] = [i]
        for k, j  in enumerate(nums):
            if (target - j ) in nums_dict:
                if j == (target-j ) :
                 if len(nums_dict[j]) >= 2 :
                    return [ nums_dict[j][0], nums_dict[j][1]]
                else:
                    if k < nums_dict[target - j][0]:
                        return [k, nums_dict[target - j][0]]
                    return [nums_dict[target-j][0],k]
        return [0,1]
                    

            


        
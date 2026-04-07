class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]* len(nums)
        product = 1
        for i in range(0,len(nums)):
            if i == 0:
                left[i] = 1
            else:
                left[i] = product
            product = product * nums[i]
        product = 1
        for j in range(len(nums)-1, -1,-1):
            if j == len(nums)-1:
                right[j] = 1
            else:
                right[j] = product
            product = product * nums[j]
        print(left)
        print(right)
        for k in range(len(nums)):
            left[k] = left[k]* right[k]
        return left




        

            
        
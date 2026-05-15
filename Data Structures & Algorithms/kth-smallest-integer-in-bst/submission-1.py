# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def findKthSmallest(root,k):
            if root :
                left = findKthSmallest(root.left,k)
                k[0] = k[0] - 1
                if k[0] == 0:
                    print("reached ")
                    return root.val
                right = findKthSmallest(root.right, k)
                if left != -1 :
                    return left 
                elif right != -1:
                    return right 
                else : 
                    return -1
            return -1
            
        return findKthSmallest(root, [k])
        
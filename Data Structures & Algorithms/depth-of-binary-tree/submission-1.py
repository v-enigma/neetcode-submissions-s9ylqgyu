# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(root, i):
            if root :
                return max( depth(root.right, i+1), depth(root.left, i+1))
                #return max(left, right)
            else:
                return i-1
        return depth(root, 1)


        
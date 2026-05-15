# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrderTraversal(root):
            if root :
                left = inOrderTraversal(root.left)
                left = (left + str(root.val)) if left else (str(root.val))
                #print(left)
                right = inOrderTraversal(root.right)
                left = (left + right) if right else (left)
                #print(left)
                return left
        result = inOrderTraversal(root)
        print(result)
        if result :
            return int(result[k-1])
        else:
            return -1

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root :
            if root.left == None and root.right == None :
                return True
            elif root.left and root.right:
                return (root.val > root.left.val and root.val < root.right.val) and self.isValidBST(root.left) and self.isValidBST(root.right)
            elif root.left :
                return (root.val > root.left.val ) and self.isValidBST(root.left)
            else :
                return (root.val < root.right.val ) and self.isValidBST(root.right)
        return True

        
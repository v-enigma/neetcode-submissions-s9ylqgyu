# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def height(node):
            if  not node :
                return -1
            return max(height(node.left), height(node.right)) + 1

        def isTreeEqual(tree1, tree2 ):
            if tree1 == None and tree2== None :
                return True
            elif tree1 == None or tree2 == None:
                return False 
            else :
                return isTreeEqual(tree1.left, tree2.left) and isTreeEqual(tree1.right, tree2.right) and tree1.val == tree2.val

        if not root:
            return False
        if height(root) == height(subRoot) and isTreeEqual(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    

        
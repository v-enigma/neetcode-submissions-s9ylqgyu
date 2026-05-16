# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[TreeNode]:
        if len(preOrder) == 0:
            return None
        if len(preOrder) == 1:
            return TreeNode(val = preOrder[0])
        else:
            
            root_val = preOrder[0]
            #print(len(preOrder), root_val)
            print(inOrder)
            print(len(inOrder), root_val)
            index = inOrder.index(root_val)
            root = TreeNode(val = root_val)
            root.left = self.buildTree(preOrder[1:index+1], inorder[0:index])
            root.right = self.buildTree(preOrder[index+1: len(preOrder)], inOrder[index+1:len(inOrder)])
            return root
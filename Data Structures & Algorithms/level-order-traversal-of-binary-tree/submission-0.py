# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q1 = []
        q2 = []
        final_result = []
        def process_queue(q1,q2):
            result = []
            while len(q1) > 0 :
                item = q1.pop(0)
                if item.left:
                        q2.append(item.left)
                if item.right :
                        q2.append(item.right)
                result.append(item.val)
            return result
        
        if root:
            q1.append(root)
                   
        while len(q1) > 0 or len(q2) > 0 :
            if len(q1) > 0 :
                final_result.append(process_queue(q1, q2))
            else:
                final_result.append(process_queue(q2,q1))
        return final_result
                




        
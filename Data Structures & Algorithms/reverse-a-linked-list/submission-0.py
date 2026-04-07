# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        while(head):
            nodeList.append(head)
            head = head.next
        i = len(nodeList)-1
        print(nodeList)
        while( i> 0):
            nodeList[i].next = nodeList[i-1]
            i = i-1
        if len(nodeList)!=0:
            nodeList[0].next = None
            return nodeList[len(nodeList)-1]
        return head
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        reverse = head
        stack = []
        while(reverse):
            stack.append(reverse)
            reverse = reverse.next
        
        i = 0
        j = len(stack)-1
        temp = head
        while i < len(stack)//2 :
            temp = head.next
            head.next = stack[j]
            stack[j].next = temp
            head = temp
            i = i + 1
            j = j-1
        if len(stack)%2 == 1:
            temp.next = stack[j]
            stack[j].next = None
        else:
            stack[j+1].next = None
        
        
        

        
        
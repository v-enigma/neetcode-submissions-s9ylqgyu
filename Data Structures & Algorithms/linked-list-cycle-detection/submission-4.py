# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        initial = True
        pointer1 = head
        if not pointer or not pointer1:
            return False
        while(pointer and pointer1 and (initial or pointer != pointer1)  ):
            if initial:
                initial = False
            pointer1 = pointer1.next
            pointer = pointer.next
            if pointer:
                pointer = pointer.next
            else:
                break
        if not pointer or not pointer1 :
            return False
        if pointer == pointer1:
            return True
        else:
            return False

        
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def countNodes()-> int:
            temp = head
            count = 0
            while temp :
                count = count + 1
                temp = temp.next
            return count
        count = countNodes()
        IndexfromStart = (count)-n +1
        prev = -1
        current = head
        index = 1
        while index <= count:
            if index == IndexfromStart:
                if prev == -1:
                    temp = current.next
                    current.next = None
                    return temp
                else:
                    prev.next = current.next
                    current.next  = None
                    return head
            prev = current
            current = current.next
            index = index + 1



        
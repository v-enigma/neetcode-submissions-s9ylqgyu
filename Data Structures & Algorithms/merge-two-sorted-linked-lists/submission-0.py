# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        Top = None
        while(list1 and list2):
            if (list1.val)<= list2.val:
                if not result :
                    result = list1
                    Top = result
                else:
                    result.next = list1
                    result = result.next
                list1 = list1.next
            else:
                if not result :
                    result = list2
                    Top = result
                else:
                    result.next = list2
                    result = result.next
                list2 = list2.next
        if(list1):
            if not result:
                result = list1
                Top = result
            else:
                result.next = list1
        if (list2):
            if not result:
                result = list2
                Top = result
            else:
                result.next = list2
        return Top
            
            

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2)-> List:
          
            
            result = ListNode()
            dummy = result
            while list1!= None and list2!= None:
                if list1.val < list2.val:
                    
                    result.next = list1
                    list1 = list1.next
                    result = result.next
                else:
                    result.next = list2
                    list2 = list2.next
                    result =result.next
                
            if list1 != None:
                result.next = list1
            if list2 != None:
                result.next = list2
                
            return dummy.next
        
        while len(lists) >= 2:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            result = mergeTwoLists(list1, list2)
            lists.append(result)
        
        #print(len(lists))
        result = lists[0] if len(lists) > 0 else None

        return result


                 
            
        
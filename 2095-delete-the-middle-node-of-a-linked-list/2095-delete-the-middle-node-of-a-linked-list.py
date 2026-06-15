# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
#         n = 0
#         node = head
        
#         while node:
#             n += 1
#             node = node.next
#         ans = tail = ListNode()
#         node = head
        
#         for i in range(n):
#             if i == int(n/2):
#                 node = node.next
#                 continue
                
#             tail.next = ListNode(node.val)
#             tail = tail.next
#             node = node.next
            
#         return ans.next
    
        if not head.next: return head.next
        ptr1, ptr2 = head, head.next
        while ptr2.next and ptr2.next.next:
            ptr2 = ptr2.next.next
            ptr1 = ptr1.next
        ptr1.next = ptr1.next.next
        return head
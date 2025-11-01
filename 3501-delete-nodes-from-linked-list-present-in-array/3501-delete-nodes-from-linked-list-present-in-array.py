# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hashT = set(nums)
        A = []
        while head:
            if head.val in hashT: 
                head = head.next
                continue
            A.append(head.val)
            head = head.next
        res = tail = ListNode(-1)
        for num  in A:
            tail.next = ListNode(num)
            tail = tail.next
        return res.next
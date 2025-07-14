# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binary = []
        while head:
            binary.append(head.val)
            head = head.next
            
        dec = 0
        binary.reverse()
        
        for i in range(len(binary)):
            if binary[i] == 1: dec += pow(2,i)
    
        return dec
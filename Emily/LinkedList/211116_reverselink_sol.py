# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur=head
        pre=None
        
        while cur:
            c=cur.next
            cur.next=pre
            
            pre=cur #first jump pre one step forward
            cur=c #then jump cur, avoid assign c to pre
        return pre

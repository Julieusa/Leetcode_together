# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        else:
            dummy=ListNode(-1) #assign a value
            dummy.next=head #storage item
            new_list=dummy #iteration item
            while new_list.next: #since append -1 at the begining so the first element is checked
                if new_list.next.val!=val:
                    new_list=new_list.next
                else:
                    new_list.next=new_list.next.next
                #print(new_list) #shorter after each run
            return dummy.next

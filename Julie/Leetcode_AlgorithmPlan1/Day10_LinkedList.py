# Q1: Merge two sorted list 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val # the head value
#         self.next = next # all the next node value
#recursion O(n+m) time | O(n+m) space
#The first call to mergeTwoLists does not return until the ends of both l1 and l2 have been reached, so n + mn+m stack frames consume O(n + m)O(n+m) space. 

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 is None:
#             return list2
#         elif list2 is None:
#             return list1
#         elif list1.val < list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2

        
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1) #set up a false "prehead" node, val=-1

        prev = prehead # prev pointer
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

      
 # Q2: Reverse linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# A node does not have reference to its previous node, you must store its previous element beforehand. You also need another pointer to store the next node before changing the reference. 
class Solution(object):        
    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
        
#     def reverseList_v1(self, head):  # Recursive
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """     
#         if not head or not head.next:
#             return head
#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return p 
        
        

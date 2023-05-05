# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        new_node=ListNode(0)
        dummy=new_node

        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                new_node.next=l1
                l1=l1.next
                #point to the smallest
            else:
                new_node.next=l2
                l2=l2.next
            new_node=new_node.next #like i=i+1
        #print(new_node)    
        new_node.next = l1 or l2 #when one list is not finished, link to the point haven't read in, something like new_node[i:]=l1[i:].
        #print(new_node)
        return dummy.next
    #exclude the begining 0 dummy.next=dummy[1:]
    #dummy is a pointer to new_node which is initialized to ListNode(0). Keep in mind that dummy is updated whenever you have something like new_node.next = .... but dummy is not updated when you have something like new_node = new_node.next. In this case new_node becomes a shorter linked list. 

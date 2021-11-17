class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        else:
            dummy=head
            #new_node=dummy
            while head.next:
                if head.val==head.next.val:
                    head.next=head.next.next
                else:
                    #dummy=head
                    head=head.next
            return dummy
          
          #previously overuse the new_node (see the comment out line), but turns out 2 pointer is enough, once assign head to dummy, then dummy does not need to assign for remove questions.
          #head is a pointer than shorter than dummy, dummy will link the rest
    """  
    def deleteDuplicates(self, head):
        cur = head
        while cur: #avoid duplicate situation head=[] or head=[1]
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
        """  

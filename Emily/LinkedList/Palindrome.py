#9
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif str(x)==str(x)[::-1]: #-1 means backwards [<start>:<stop>:<step>]
            #print(str(x),str(x)[::-1])
            return True
          
#234. Palindrome Linked List
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list1=[]
        while head:
            list1.append(str(head.val))
            head=head.next
        #print(list1)
        str_head=''.join(list1)
        if str_head==str_head[::-1]:
            return True

 #alter sol
def isPalindrome(self, head):
    # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
    rev = None
    # initially slow and fast are the same, starting from head
    slow = fast = head
    while fast and fast.next:
        # fast traverses faster and moves to the end of the list if the length is odd
        fast = fast.next.next
        
        # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
       # fast is at the end, move slow one step further for comparison(cross middle one)
        slow = slow.next
    # compare the reversed first half with the second half
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    
    # if equivalent then rev become None, return True; otherwise return False 
    return not rev
  
#125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_s=[]
        for i in s:
            if s.isalnum(): #not number of char(sysmol)
                list_s.append(i)
            
        str_s=''.join(list_s)
        if str_s==str_s[::-1]:
            return True

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val==val:
            return root
        else:
            return self.searchBST(root.left,val) or self.searchBST(root.right,val)
            
            
            
       #others: similar iterative
      temp = root
        while temp:
            if temp.val == val: return temp
            elif temp.val < val: temp = temp.right
            else: temp = temp.left
        return None

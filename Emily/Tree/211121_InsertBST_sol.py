#701
#use recurrent
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            root=TreeNode(val)
            return root
        else:
            if root.val>val:
                root.left=self.insertIntoBST(root.left,val)
                #print(root.left)
            else:
                root.right=self.insertIntoBST(root.right,val)
                
            return root

class Solution(object):
    def findnode(self,root,array1):
        if root:
            self.findnode(root.left,array1)
            array1.append(root.val)
            self.findnode(root.right,array1)
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #iterative tree first level is always the largest among left and smallest among right
        array1=[]
        
        self.findnode(root,array1)
        #print(array1)
        for i in range(1,len(array1)):
            if array1[i-1]>=array1[i]:
                return False
            
        return True

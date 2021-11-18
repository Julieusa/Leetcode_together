class Solution(object):
    #need to write self.defined function
    def appendnode(self,root,array1):
        if root:
            array1.append(root.val)
            self.appendnode(root.left,array1)
            self.appendnode(root.right,array1)
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        array1=[]
        if not root:
            return root
        else:
            self.appendnode(root,array1)
            return array1
          
          
        #return the tree in the order of root, left node, right node e.g. [1,null, 2,3,4,5,6] 4 depth tree return [1,2,3,5,6,4].

class Solution(object):
    
    def appendnode(self,root,array1):
        if root:
            self.appendnode(root.left,array1)
            array1.append(root.val)
            self.appendnode(root.right,array1)
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        array1=[]
        if not root:
            return root
        else:
            self.appendnode(root,array1)
            return array1
          #inorder tree, return [1,5,3,6,2,4] first root, then left and final right
          
 class Solution(object):
    
    def appendnode(self,root,array1):
        if root:
            self.appendnode(root.left,array1)
            self.appendnode(root.right,array1)
            array1.append(root.val)
            
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        array1=[]
        if root:
            self.appendnode(root,array1)
        return array1
      
      
     #return [5,6,3,4,2,1] return first left and right, then root

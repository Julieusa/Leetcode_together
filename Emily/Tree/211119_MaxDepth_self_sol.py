def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
      
class Solution(object):
    #changed based on the solution of 102. Binary Tree Level Order Traversal
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #array1=[]
        count=0
        level=[root]
        while root and level:
            #currentnode=[]
            nextnode=[]
            for node in level:
                #count+=1
                #currentnode.append(node.val)
                if node.left:
                    nextnode.append(node.left)
                if node.right:
                    nextnode.append(node.right)
            #array1.append(currentnode)
            count+=1
            level=nextnode
            #self.findnext(root,count)            
        
        return count

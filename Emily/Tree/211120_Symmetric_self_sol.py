#101 


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #array1=[]
        level=[root]
        while root and level:
            currentnode=[]
            nextnode=[]
            for node in level:
                if node:
                    currentnode.append(node.val)
                    for child in (node.left,node.right):
                        nextnode.append(child)
                else:
                    currentnode.append(None)
                level=nextnode
            if currentnode != currentnode[::-1]: #A[::-1] is from [1,2,3,4] to [4,3,2,1]
                return False
        return True  
      
      
      #short:
      def isSymmetric(self, root):
        queue = [root]
        while queue:
            values = [i.val if i else None for i in queue]
            if values != values[::-1]: return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True
      
      #recurrent
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left,root.right)
    
    def dfs(self,L,R):
        if L and R:
            print(L,R)
            return L.val==R.val and self.dfs(L.left,R.right) and self.dfs(R.left,L.right)
        return L==R
      
      #change from tree order:
      
      def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        array1=[]
        level=[root]
        while root and level:
            currentnode=[]
            nextnode=[]
            for node in level:
                if node:
                    currentnode.append(node.val)
                    for child in (node.left,node.right):
                        nextnode.append(child)
                else:
                    currentnode.append(None)
                level=nextnode
            
            array1.append(currentnode)
              
        for i in array1:
            if i>=1:
                #print(i)
                for j in range(len(i)/2):
                    if i[j]!=i[-1-j]:
                        return False
        return True
      

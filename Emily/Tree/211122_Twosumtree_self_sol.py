#635
class Solution(object):
    def findnode(self,root,array1):
        if root:
            self.findnode(root.left,array1)
            array1.append(root.val)
            self.findnode(root.right,array1)
            
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        array1=[]
        self.findnode(root,array1)
        dict_={}
        for loc,item in enumerate(array1):
            if item in dict_:
                return True
            else:
                dict_[k-item]=loc
                
        return False
      
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        return self._findTarget(root, set(), k)
    
    def _findTarget(self, node, nodes, k):
        if not node:
            return False

        complement = k - node.val
        if complement in nodes:
            return True

        nodes.add(node.val)

        return self._findTarget(node.left, nodes, k) or self._findTarget(node.right, nodes, k)

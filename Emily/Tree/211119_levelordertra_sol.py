# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        array1=[]
        level=[root] #level is similiarly to linked list, where root.left/right is the next pointer
        #print(level)
        while root and level:
            currentnode=[]
            nextnode=[]
            for node in level:
                currentnode.append(node.val)
                if node.left:
                    nextnode.append(node.left)
                if node.right:
                    nextnode.append(node.right)
                
            array1.append(currentnode)
            level=nextnode
            #print(level)
        
        return array1

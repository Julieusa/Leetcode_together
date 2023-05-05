# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#need to work on
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        '''level=[root]
        while level:
            sum_=0
            nextnode=[]
            for node in level:
                if node:
                    if node.val+sum_==targetSum:
                        return True
                    elif node.val+sum_<targetSum:
                        sum_+=node.val
                        for child in (node.left,node.right):
                            nextnode.append(child)
                        #if node.left.val+sum_<=targetSum:
                        #    nextnode.append(node.left)
                        #if node.right.val+sum_<=targetSum:
                        #    nextnode.append(node.right)
                        #if node.left.val+sum_>targetSum and node.right.val_sum_>targetSum:
                        #    return False
                    else:
                        return False
                else:
                    return False
            level=nextnode
            print(sum_)
        return True'''
    #use subtract instead of add
    #def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True
        
        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

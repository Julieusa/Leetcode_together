#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:58:59 2021

@author: emily
"""

class Solution(object):

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root:
            if root.val<low:
                return self.rangeSumBST(root.right,low,high) #need to use return function so the return is a value
            if root.val>high:
                return self.rangeSumBST(root.left,low,high)
            if low<=root.val<=high:
                return root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)
        else:
            return 0 #this is required
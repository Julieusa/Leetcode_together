#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:51:50 2021

@author: emily
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findsum(self,root,low,high):
        if root:
            #print(sum_)
            if root.val>high:
                self.findsum(root.left,low,high)
            elif root.val<low:
                self.findsum(root.right,low,high)
            elif low<=root.val<=high:
                self.sum_+=root.val
                self.findsum(root.left,low,high)
                self.findsum(root.right,low,high)
            
    
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum_=0 #this will accumulate
        self.findsum(root,low,high)
        return self.sum_
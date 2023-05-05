#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:42:29 2021

@author: emily
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result=[]
        forward=0
        #i,j=0,0
        i,j=len(num1)-1,len(num2)-1
        while i>=0 or j>=0: #avoid using num[-i-1], count down
            if i>=0:
                x1=ord(num1[i])-ord('0')
            else:
                x1=0 #use 0 in the summation so auto disappears
            if j>=0:
                x2=ord(num2[j])-ord('0')
            else:
                x2=0
                
            value=(x1 + x2 + forward) % 10 #return digit
            forward=(x1 + x2 + forward)//10 #return forward 48//10=4
            result.append(value)
        
            i-=1
            j-=1
        if forward:
            result.append(forward)
        return ''.join(str(x) for x in result[::-1])
                
        
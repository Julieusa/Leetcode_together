#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:35:39 2021

@author: emily
"""
#680 Valid Palindrome II
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==s[::-1]:
            return True
        else:
            p1=0
            p2=len(s)-1
            #count=0
            while p1<p2:
                if s[p1]!=s[p2]:
                    string_front=s[:p1]+s[p1+1:]
                    string_back=s[:p2]+s[p2+1:]
                    return string_front==string_front[::-1] or string_back==string_back[::-1]
                else:
                    p1+=1
                    p2-=1
            return False
            
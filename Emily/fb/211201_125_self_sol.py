#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:26:52 2021

@author: emily
"""
#125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #s=s.replace('.','')
        #s=s.replace(',','')
        #s=s.replace(':','')
        #s= s.replace(' ', '')
        s=lower(s)
        string_s=[]
        for j in s:
            if j.isalnum(): #not num or char
                string_s.append(j)
        s=''.join(string_s)
        """
        if len(s)==0 or len(s)==1:
            return True
        else:
            stack_s=[]
            for i in range(len(s)):
                if i<len(s)/2:
                    stack_s.append(s[i])
                    print(i)
                else:
                    if s[i]==stack_s[-1]:
                        stack_s.pop()
            return len(stack_s)==0
        """
        #sol:
        return s==s[::-1]
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:50:37 2022

@author: Samad
"""

def check_anagram(a,b):
    d1={}
    d2={}
    if len(a)!=len(b):
        return 'Not a Anagram'
    else:
        for i in range(len(a)):
            if a[i] not in d1:
                d1[a[i]]=a.count(a[i])
        for j in range(len(b)):
            if b[j] not in d2:
                d2[b[j]]=b.count(b[j])
        print(d1,d2)
        if d1==d2:
            return 'Anagram'
        else:
            return 'Not a Anagram'
  

inp1=input('Enter String : ')
inp2=input('Enter string to check whether it is anagram or not :')
print(check_anagram(inp1,inp2))
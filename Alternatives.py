# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:35:07 2019

@author: omer
"""
from Fundamentals import Mtrx

def MtrxMltpl2(A,B,n='natural',m='natural'):
    #A, B should be matices in dictionary form
    #n number of lines, m number of rows, of desired product
    if n=='natural':
        n=A['n']
    if m=='natural':
        m=B['m']
    L=[]
    for i in range(n):
        for j in range(m):
            Val=0
            for k in range(max(n,m)):
                try:
                    Val+=A[(i,k)]*B[(k,j)]
                except:
                    continue
            L.append(Val)
    return Mtrx(L,n,m)
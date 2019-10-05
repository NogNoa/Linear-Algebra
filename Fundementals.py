# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:19:16 2019

@author: omer
"""

def CnstrctםMtrx(L,n):
    #L should be a list
    Mat={}
    for i in range(n**2):
        try:
            Mat[(i//n,i%n)]=L[i]
        except:
            Mat[(i//n,i%n)]=0
    return Mat
def MtrxםMltpl(A,B):
    #A, B should be matices in dictionary form
    C={}
    for i in range(2):
        for j in range(2):
            C[(i,j)]=0
            for k in range(2):
                C[(i,j)]+=A[(i,k)]*B[(k,j)]
    return C
A=CnstrctםMtrx([1,2,3,4,5],3)
B=CnstrctםMtrx([2,0,0,2],2)
C=MtrxםMltpl(A,B)
def CnstrctMtrx(L,n,m):
    #L should be a list
    Mat={}
    for i in range(n*m):
        try:
            Mat[(i//m,i%m)]=L[i]
        except:
            Mat[(i//m,i%m)]=0
    return Mat
def MtrxMltpl(A,B,n,m):
    #A, B should be matices in dictionary form
    C={}
    kull=min(n,m)
    for i in range(n):
        for j in range(m):
            C[(i,j)]=0
            for k in range(kull):
                try:
                    C[(i,j)]+=A[(i,k)]*B[(k,j)]
                except:
                    C[(i,j)]+=0
    return C
A=CnstrctMtrx([1,2,3,4,5],2,3)
B=CnstrctםMtrx([2,0,0,2],2)
C=MtrxMltpl(A,B,2,2)
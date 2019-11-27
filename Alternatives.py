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

def Mtrx2(L,n,m='natural'):
    #L should be a list, n number of lines, m number of rows
    Mat={}
    λ=len(L)
    if m=='natural':
        #we only need the collomn argument,
        #but the linear-algebra savvy user 
        #expect the order to be n,m when he
        #enters two arguments.
        m=n 
        n=int(λ/m+(λ/m)%1) #rounding up λ/m
    for i in range(λ):
        Mat[(i//m,i%m)]=L[i]
    for i in range(λ,n*m):
        Mat[(i//m,i%m)]=0
    Mat['n'],Mat['m']=n,m
    return Mat

A=Mtrx2([1,2,3,4,5,6,7],3,6)

#ToDo: unite MtrxMltpl and QuickMltply

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:19:16 2019

@author: omer
"""
def Mtrx(L,n,m='same'):
    #L should be a list, n number of lines, m number of rows
    if m=='same':
        m=n
    Mat={}
    for i in range(n*m):
        try:
            Mat[(i//m,i%m)]=L[i]
        except:
            Mat[(i//m,i%m)]=0
    return Mat
def MtrxMltpl(A,B,n,m='same'):
    #A, B should be matices in dictionary form
    #n number of lines, m number of rows, of desired product
    if m=='same':
        m=n
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
def SclrMltpl(A,s):
    #A should be matix, s an integer
    Scal={}
    for i in A:
        Scal[i]=A[i]*s
    return Scal
def IMtrx(n,s=1):
    Mat={}
    for i in range(n):
        for k in range(n):
            if k==i:
                Mat[k,k]=s
            else:
                Mat[i,k]=0
    return Mat
        
A=Mtrx([1,2,3,4,5],2,3)
B=Mtrx([2,0,0,2],2)
C=MtrxMltpl(A,B,2)
D=(SclrMltpl(A,2))
E=MtrxMltpl(A,IMtrx(2,2),2,3)
F=IMtrx(3)
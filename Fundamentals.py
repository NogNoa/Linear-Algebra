# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:19:16 2019

@author: omer
"""
from math import ceil


def Same(a, b):
    if a == 'same':
        return b
    return a


def Mtrx(L,n,m='natural'):
    # L should be a list, n number of lines, m number of rows
    Mat = {}
    λ = len(L)
    if m == 'natural':
        """we only need the collumn argument,
        but the linear-algebra savvy user 
        expect the order to be n,m when he
        enters two arguments.
        """
        m=n 
        n=ceil(λ/m)
    for i in range(λ):
        Mat[(i//m,i%m)] = L[i]
    for i in range(λ,n*m):
        Mat[(i//m,i%m)] = 0
    Mat['n'], Mat['m'] = n, m
    return Mat


def IMtrx(n,s=1):
    Mat = {}
    for i in range(n):
        for k in range(n):
            if k == i:
                Mat[k,k]=s
            else:
                Mat[i,k]=0
    Mat['n'],Mat['m']=n,n
    return Mat


def PrntMtrx(A):
    for i in range(A['n']):
        p=''
        for j in range(A['m']):
            p+=',  '*(j!=0)+str((A[i,j]))
        print(p)
    print()
    return


def MtrxMltply(A,B,n='natural',m='natural'):
    """A, B should be matices in dictionary form
    n number of lines, m number of rows, of desired product
    """
    if n=='natural':
        n=A['n']
    if m=='natural':
        m=B['m']
    Mat={}
    lum=min(A['m'],B['n'])
    for i in range(n):
        for j in range(m):
            Mat[(i,j)]=0
            for k in range(lum):
                Mat[(i,j)]+=A[(i,k)]*B[(k,j)]
    Mat['n'],Mat['m']=n,m
    return Mat


def SclrMltply(A,s):
    # A should be matrix, s an integer
    Scal={}
    for i in A:
        Scal[i]=A[i]*s
    return Scal


def reWrite(A,n='same',m='same'):
    #if n =='same':
        #n = A['n']
    n = Same(n, A['n'])
    if m == 'same':
        m = A['m']
    # m=Same(m,A['m'])
    Mat = {}
    for i in range(n):
        for j in range(m):
            if (i,j) in A:
                 Mat[(i,j)] = A[(i,j)]
            else:
               Mat[(i,j)] = 0
    Mat['n'],Mat['m'] = n,m
    return Mat


def QuickMltply(L,n,R='same',m='same'):
    m = Same(m,n)
    R = Same(R,L)
    Mat = MtrxMltply(Mtrx(L,n),Mtrx(R,m))
    PrntMtrx(Mat)
    return Mat 


A = Mtrx([1,2,3,4,5],2)
#B = Mtrx([6,4,3,1],1)
#C = MtrxMltply(A,B)
#D = SclrMltply(A,2)
#F = MtrxMltply(IMtrx(3,2),IMtrx(3,2))
E = reWrite(A, 1, 1)
#G = QuickMltply([.8, .1, .2, .9], 2)
PrntMtrx(A)

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:19:16 2019

@author: omer
"""
def Mtrx(L,m,n='natural'):
    #L should be a list, n number of lines, m number of rows
    Mat={}
    λ=len(L)
    if n=='natural':
        n=(λ//m)+1
    for i in range(λ):
        Mat[(i//m,i%m)]=L[i]
    for i in range(λ,n*m):
        Mat[(i//m,i%m)]=0
    Mat['n'],Mat['m']=n,m
    return Mat

def IMtrx(n,s=1):
    Mat={}
    for i in range(n):
        for k in range(n):
            if k==i:
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
    return

def MtrxMltpl(A,B,n='natural',m='natural'):
    #A, B should be matices in dictionary form
    #n number of lines, m number of rows, of desired product
    if n=='natural':
        n=A['n']
    if m=='natural':
        m=B['m']
    Mat={}
    for i in range(n):
        for j in range(m):
            Mat[(i,j)]=0
            for k in range(max(n,m)):
                try:
                    Mat[(i,j)]+=A[(i,k)]*B[(k,j)]
                except:
                    continue
    Mat['n'],Mat['m']=n,m
    return Mat

def SclrMltpl(A,s):
    #A should be matix, s an integer
    Scal={}
    for i in A:
        Scal[i]=A[i]*s
    return Scal

A=Mtrx([1,2,3,4,5],2,3)
B=Mtrx([6,4,3,1],2)
D=SclrMltpl(A,2)
F=MtrxMltpl(IMtrx(3,2),IMtrx(3,2))
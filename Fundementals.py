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

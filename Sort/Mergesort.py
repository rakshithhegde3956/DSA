
def merge(a, l, m, r):

    n1 = m-l+1
    n2 = r-m


    l1 = [0] * n1
    r1 = [0] * n2

    for i in range(n1):
        l1[i] = a[l+i]

    for i in range(n2):
        r1[i] = a[m+1+i]

    i=0
    j=0
    k=l

    while i<n1 and j<n2:
        if l1[i]<r1[j]:
            a[k]=l1[i]
            i+=1
        
        else :
            a[k]=r1[j]
            j+=1

        k+=1

    
    while j!=n2:
        a[k]=r1[j]
        k+=1
        j+=1
    
    while i!=n1:
        a[k]=l1[i]
        k+=1
        i+=1

def sort(a, l, r):

    if(l<r):
        m=(l+(r-1))//2

        sort(a, l, m)
        sort(a, m+1, r)
        merge(a,l,m,r)
        

a=[5,4,7,2,3,1]
n=len(a)

sort(a, 0 , n-1)

print("Soreted array:", a)


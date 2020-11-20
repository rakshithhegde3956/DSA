

def partition(a, l, r):
    p=a[l]
    i=l


    while(True):

        while(l<=r and a[l]<=p):
            l+=1
        
        while(l<=r and a[r]>=p):
            r-=1
        
        if(l<=r):
            temp=a[l]
            a[l]=a[r]
            a[r]=temp

        else:
            break

    temp=a[r]
    a[r]=a[i]
    a[i]=temp

    return r


def sort(a, l, r):

    if len(a)==1:
        return a

    if l<r:
        p=partition(a, l, r)

        sort(a, l, p-1)
        sort(a, p+1, r)

    
        

a=[5,4,7,2,3,1, 3, 6, 8, 2, 4]
n=len(a)

sort(a, 0 , n-1)

print("Soreted array:", a)




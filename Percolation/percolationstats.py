import sys
import random as r
from percolation import Percolation as perc


if __name__=="__main__":
    t=40
    sumOpen = []

    args = sys.argv
    if len(args) > 1:
        t = int(sys.argv[1])

    for i in range(t):
        n=20

        p=perc(n)

        while(p.percolates()!=True):
            k = r.randint(1,n**2)-1
            p.open(int(k/n),k%n) 
        
        sumOpen.append(p.openSites())
        
    print(sumOpen)

    print("Mean",(sum(sumOpen)/t)/(n**2))

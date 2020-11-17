from unionfind import UnionFind as uf
import sys
import random as r

class Percolation:

    def __init__(self, n):
        self.grid= [[0 for i in range(n)] for j in range(n)]
        self.u = uf(n**2)

    def showGrid(self):
        for i in range(len(self.grid)):
            print(self.grid[i])

        
    def isOpen(self, row, col):
        return self.grid[row][col]

    def open(self, row, col):
        self.grid[row][col]=1
        self.union(row,col)
        #print(self.grid)

    def openSites(self):
        #print(self.grid)
        return sum(map(sum,self.grid))
    
    def union(self,row,col):
        l=len(self.grid)
        i=row*l+col

        if(col+1<l):
            if(self.grid[row][col+1]==1):
                self.u.union(i, i+1)

        if(col-1>=0):
            if(self.grid[row][col-1]==1):
                self.u.union(i, i-1)
        
        if(row+1<l):
            if(self.grid[row+1][col]==1):
                self.u.union(i, i+l)

    def percolates(self):
        l=len(self.grid)
        size=l**2
        for i in range(l):
            for j in range(size-l,size):
                if(self.u.find(i,j)):
                    #self.showGrid()
                    #print("Percolates", self.openSites())
                    return True
        #print("Does not percolate", self.openSites())
        return False
    
  
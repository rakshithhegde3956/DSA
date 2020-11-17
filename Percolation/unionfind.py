class UnionFind:

    def __init__(self, size):
        self.size = size
        self.id = list(range(size))
        self.depth = [1] * size

    def root(self, p):
        #print("root", p, self.id[p])
        while(p!=self.id[p]):
            self.id[p]= self.id[self.id[p]]
            p=self.id[p]
            #print("root inside while", p, self.id[p])
        return p


    def find(self, p,q):
        #print("find", p,q)
        return self.root(p)==self.root(q)
    
    def union(self, p, q):
        #print("union", p,q)
        i=self.root(p)
        j=self.root(q)

        if(self.depth[i] < self.depth[j]):
            self.id[i] = j
            self.depth[j]+=self.depth[i]
        else:
            self.id[j] = i
            self.depth[i]+=self.depth[j]


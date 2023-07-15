class UnionFind():
    """
    Union-Find Tree

    Attributes
    ----------
    n : int
        number of nodes
    parents : list
        parents of nodes
    rank : list
        depth of trees
    """

    def __init__(self, n):
        """
        Parameters
        ----------
        n : int
            number of nodes
        """
        self.n = n
        self.parents = [-1] * n
        self.rank = [0] * n
    
    def find(self, x):
        """
        find parent of node x
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        """
        unite nodes x and y
        if x and y are in the same tree, return False
        else, return True
        """
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        elif self.rank[x] > self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
        else:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
        return True
    
    def size(self, x):
        """
        size of tree which node x belongs to
        """
        return -self.parents[self.find(x)]
    
    def same(self, x, y):
        """
        if x and y are in the same tree, return True
        """
        return self.find(x) == self.find(y)
    
    def roots(self):
        """
        return list of roots
        """
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        """
        return number of trees
        """
        return len(self.roots())
    
    def all_group_members(self):
        """
        return dict of {root: [members]}
        """
        return {r: self.members(r) for r in self.roots()}
    

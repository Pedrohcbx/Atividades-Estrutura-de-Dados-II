class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

    def split(self, i, y):
        z = BTreeNode(y.t, y.leaf)
        z.keys = y.keys[self.t:]
        if not y.leaf:
            z.children = y.children[self.t:]
        y.keys = y.keys[:self.t - 1]
        y.children = y.children[:self.t]
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

    def insert_non_full(self, k):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(k)
            self.keys.sort()
        else:
            while i >= 0 and k < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split(i, self.children[i])
                if k > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(k)

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and k == self.keys[i]:
            return True
        if self.leaf:
            return False
        return self.children[i].search(k)

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, k):
        r = self.root
        if len(r.keys) == 2 * self.t - 1:
            s = BTreeNode(self.t, False)
            s.children.insert(0, r)
            s.split(0, r)
            i = 0
            if k > s.keys[0]:
                i += 1
            s.children[i].insert_non_full(k)
            self.root = s
        else:
            r.insert_non_full(k)

    def search(self, k):
        return self.root.search(k)

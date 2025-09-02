from graphviz import Digraph
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node: return Node(value)
        if value < node.value: node.left = self._insert(node.left, value)
        else: node.right = self._insert(node.right, value)
        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node: return False
        if node.value == value: return True
        return self._search(node.left, value) if value < node.value else self._search(node.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node: return node
        if value < node.value: node.left = self._delete(node.left, value)
        elif value > node.value: node.right = self._delete(node.right, value)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)
        return node

    def _min_value_node(self, node):
        while node.left: node = node.left
        return node

    def height(self, node=None):
        if node is None: node = self.root
        if not node: return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def depth(self, value):
        return self._depth(self.root, value, 0)

    def _depth(self, node, value, d):
        if not node: return -1
        if node.value == value: return d
        return self._depth(node.left, value, d+1) if value < node.value else self._depth(node.right, value, d+1)

    def draw(self):
        dot = Digraph()
        def _draw(node):
            if not node: return
            dot.node(str(id(node)), str(node.value))
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)))
                _draw(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)))
                _draw(node.right)
        _draw(self.root)
        return dot

# Árvore fixa
tree = BinarySearchTree()
for v in [55, 30, 80, 20, 45, 70, 90]:
    tree.insert(v)
dot_fixed = tree.draw()
dot_fixed.render("bst_fixa", format="png", cleanup=True)

print("Busca 45:", tree.search(45))
tree.delete(30)
tree.insert(100)
print("Altura:", tree.height())
print("Profundidade de 45:", tree.depth(45))

# Árvore randômica
tree2 = BinarySearchTree()
nums = random.sample(range(1,200), 15)
for n in nums: tree2.insert(n)
dot_rand = tree2.draw()
dot_rand.render("bst_random", format="png", cleanup=True)

print("Árvore fixa em bst_fixa.png")
print("Árvore randômica em bst_random.png")
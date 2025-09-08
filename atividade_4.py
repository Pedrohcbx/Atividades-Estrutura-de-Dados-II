from graphviz import Digraph
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root: return Node(key)
        if key < root.value: root.left = self.insert(root.left, key)
        else: root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Rotations
        if balance > 1 and key < root.left.value: return self.right_rotate(root)
        if balance < -1 and key > root.right.value: return self.left_rotate(root)
        if balance > 1 and key > root.left.value:
            root.left = self.left_rotate(root.left); return self.right_rotate(root)
        if balance < -1 and key < root.right.value:
            root.right = self.right_rotate(root.right); return self.left_rotate(root)
        return root

    def get_height(self, node): return node.height if node else 0
    def get_balance(self, node): return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def left_rotate(self, z):
        y = z.right; T2 = y.left
        y.left = z; z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left; T3 = y.right
        y.right = z; z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def draw(self, root):
        dot = Digraph()
        def _draw(node):
            if not node: return
            dot.node(str(id(node)), str(node.value))
            if node.left:
                dot.edge(str(id(node)), str(id(node.left))); _draw(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right))); _draw(node.right)
        _draw(root)
        return dot

avl = AVLTree()
root = None
for v in [10,20,30]:
    root = avl.insert(root,v)
    avl.draw(root).render(f"avl_{v}", format="png", cleanup=True)

root2 = None
for v in [10,30,20]:
    root2 = avl.insert(root2,v)
    avl.draw(root2).render(f"avl_dupla_{v}", format="png", cleanup=True)

# Árvore randômica
root3 = None
nums = random.sample(range(1,100),20)
for n in nums: root3 = avl.insert(root3,n)
avl.draw(root3).render("avl_random", format="png", cleanup=True)

print("Árvores AVL salvas em avl_*.png")

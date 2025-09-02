from atividade_2 import BinarySearchTree
import random

# Árvore fixa
tree = BinarySearchTree()
for v in [55, 30, 80, 20, 45, 70, 90]:
    tree.insert(v)

def inorder(node):
    return inorder(node.left) + [node.value] + inorder(node.right) if node else []

def preorder(node):
    return [node.value] + preorder(node.left) + preorder(node.right) if node else []

def postorder(node):
    return postorder(node.left) + postorder(node.right) + [node.value] if node else []

print("Travessias árvore fixa:")
print("Inorder:", inorder(tree.root))
print("Preorder:", preorder(tree.root))
print("Postorder:", postorder(tree.root))

# Árvore randômica
tree2 = BinarySearchTree()
nums = random.sample(range(1,100), 10)
for n in nums: tree2.insert(n)

print("\nTravessias árvore randômica:")
print("Inorder:", inorder(tree2.root))
print("Preorder:", preorder(tree2.root))
print("Postorder:", postorder(tree2.root))

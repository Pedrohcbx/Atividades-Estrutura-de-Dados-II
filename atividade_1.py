from graphviz import Digraph
import random

# Classe Nó da árvore de expressão
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Função para desenhar árvore
def draw_tree(node, dot=None, parent=None):
    if dot is None:
        dot = Digraph()
    dot.node(str(id(node)), str(node.value))
    if parent:
        dot.edge(str(id(parent)), str(id(node)))
    if node.left:
        draw_tree(node.left, dot, node)
    if node.right:
        draw_tree(node.right, dot, node)
    return dot

# Construir árvore fixa: (7 + 3) * (5 - 2)
root_fixed = Node("*")
root_fixed.left = Node("+")
root_fixed.right = Node("-")
root_fixed.left.left = Node("7")
root_fixed.left.right = Node("3")
root_fixed.right.left = Node("5")
root_fixed.right.right = Node("2")

dot_fixed = draw_tree(root_fixed)
dot_fixed.render("arvore_fixa", format="png", cleanup=True)

# Criar árvore randômica
ops = ["+", "-", "*"]
def random_expr_tree():
    root = Node(random.choice(ops))
    root.left = Node(str(random.randint(1, 9)))
    root.right = Node(random.choice(ops))
    root.right.left = Node(str(random.randint(1, 9)))
    root.right.right = Node(str(random.randint(1, 9)))
    return root

root_random = random_expr_tree()
dot_random = draw_tree(root_random)
dot_random.render("arvore_random", format="png", cleanup=True)

print("Árvore fixa salva em arvore_fixa.png")
print("Árvore randômica salva em arvore_random.png")

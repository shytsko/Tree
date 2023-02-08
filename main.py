from simple_tree import SimpleTree
from AVLTree import AVLTree
from RedBlackTree import RedBlackTree

tree = RedBlackTree()
test_items = [30, 15, 8, 1, 5, 10, 20, 35, 21, 3, 40]

for item in test_items:
    tree.insert(item)

print(tree.contains(20))
print(tree.contains(10))
print(tree.contains(18))
print(tree.contains(40))
print(tree.contains(2))
tree.remove(20)
print(tree.contains(20))
tree.remove(30)
print()
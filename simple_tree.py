import re
from tree_interface import TreeInterface


class SimpleTree(TreeInterface):
    class Node:
        def __init__(self, value) -> None:
            super().__init__()
            self.value = value
            self.left: SimpleTree.Node = None
            self.right: SimpleTree.Node = None

        def __repr__(self) -> str:
            return str(self.value)

    def __init__(self) -> None:
        super().__init__()
        self.root: SimpleTree.Node = None

    def insert(self, item):
        self.root = self.__insert(self.root, item)

    def __insert(self, node, item):
        if node is None:
            return SimpleTree.Node(item)
        if item < node.value:
            node.left = self.__insert(node.left, item)
        else:
            node.right = self.__insert(node.right, item)
        return node

    def remove(self, item):
        return self.__remove(self.root, item)

    def __remove(self, node: Node, item):
        if node is None:
            return None

        if item < node.value:
            node.left = self.__remove(node.left, item)
            return node
        if item > node.value:
            node.right = self.__remove(node.right, item)
            return node

        if node.left is None and node is None:
            return None
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            min_value = self.__find_min(node.right).value
            node.value = min_value
            node.right = self.__remove(node.right, min_value)
            return node

    def __find_min(self, node: Node) -> Node:
        if node.left is not None:
            return self.__find_min(node.left)
        else:
            return node

    def contains(self, item) -> bool:
        return self.__contains(self.root, item)

    def __contains(self, node: Node, item) -> bool:
        if node is None:
            return False
        if item == node.value:
            return True
        if item < node.value:
            return self.__contains(node.left, item)
        else:
            return self.__contains(node.right, item)

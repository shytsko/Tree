"""
Реализация красно-черного дерева
За основу взят пример отсюда: https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE-%D1%87%D1%91%D1%80%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE
"""

from tree_interface import TreeInterface
from enum import IntEnum, auto, unique


class RedBlackTree(TreeInterface):

    @unique
    class Color(IntEnum):
        RED = auto()
        BLACK = auto()

    class Node:
        def __init__(self, value: int) -> None:
            super().__init__()
            self.value: int = value
            self.left: RedBlackTree.Node = None
            self.right: RedBlackTree.Node = None
            self.parent: RedBlackTree.Node = None
            self.color: RedBlackTree.Color = RedBlackTree.Color.RED

        def __repr__(self) -> str:
            return str(self.value)

    def __init__(self) -> None:
        super().__init__()
        self.root: RedBlackTree.Node = None

    def __get_grandparent(self, node: Node) -> Node:
        if node is None or node.parent is None:
            return None
        else:
            return node.parent.parent

    def __get_uncle(self, node: Node) -> Node:
        gtandparent: RedBlackTree.Node = self.__get_grandparent(node)
        if not gtandparent:
            return None
        if node.parent == gtandparent.left:
            return gtandparent.right
        else:
            return gtandparent.left


    def __rotate_left(node: Node):
        pivot: RedBlackTree.Node = node.right
        pivot.parent = node.parent
        if node.parent:
            if node.parent.left == node:
                node.parent.left = pivot
            else:
                node.parent.right = pivot
        
        node.right = pivot.left
        if pivot.left:
            pivot.left.parent = node

        node.parent = pivot
        pivot.left = node

    def __rotate_right(node: Node):
        pivot: RedBlackTree.Node = node.left
        pivot.parent = node.parent
        if node.parent:
            if node.parent.left == node:
                node.parent.left = pivot
            else:
                node.parent.right = pivot
        
        node.left = pivot.right
        if pivot.right:
            pivot.right.parent = node

        node.parent = pivot
        pivot.right = node


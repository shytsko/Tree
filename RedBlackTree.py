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

    def __rotate_left(self, node: Node):
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

    def __rotate_right(self, node: Node):
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

    def insert(self, value):
        new_node = RedBlackTree.Node(value)
        if self.root:
            place: RedBlackTree.Node = self.root
            parent: RedBlackTree.Node = None
            while place:
                parent = place
                if place.value < value:
                    place = place.right
                else:
                    place = place.left
            new_node.parent = parent
            if parent.value < new_node.value:
                parent.right = new_node
            else:
                parent.left = new_node
        else:
            self.root = new_node

        self.__fix_insert1(new_node)

    def __fix_insert1(self, node: Node):
        if not node.parent:
            node.color = RedBlackTree.Color.BLACK
        else:
            self.__fix_insert2(node)

    def __fix_insert2(self, node: Node):
        if node.parent.color == RedBlackTree.Color.BLACK:
            return
        else:
            self.__fix_insert3(node)

    def __fix_insert3(self, node: Node):
        uncle: RedBlackTree.Node = self.__get_uncle(node)
        grandparent: RedBlackTree.Node = self.__get_grandparent(node)

        if uncle and uncle.color == RedBlackTree.Color.RED:
            node.parent.color = RedBlackTree.Color.BLACK
            uncle.color = RedBlackTree.Color.BLACK
            grandparent.color = RedBlackTree.Color.RED
            self.__fix_insert1(grandparent)
        else:
            self.__fix_insert4(node)

    def __fix_insert4(self, node: Node):
        grandparent: RedBlackTree.Node = self.__get_grandparent(node)
        if node == node.parent.right and node.parent == grandparent.left:
            self.__rotate_left(node.parent)
            node = node.left
        elif node == node.parent.left and node.parent == grandparent.right:
            self.__rotate_right(node.parent)
            node = node.right
        self.__fix_insert5(node)

    def __fix_insert5(self, node: Node):
        grandparent: RedBlackTree.Node = self.__get_grandparent(node)
        node.parent.color = RedBlackTree.Color.BLACK
        grandparent.color = RedBlackTree.Color.RED
        if node == node.parent.left and node.parent == grandparent.left:
            self.__rotate_right(grandparent)
        else:
            self.__rotate_left(grandparent)

    def remove(self, value: int):
        pass

    def contains(self, value: int) -> bool:
        pass


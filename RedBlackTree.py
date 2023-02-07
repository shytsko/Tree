"""
Реализация красно-черного дерева
За основу взят пример отсюда: https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE-%D1%87%D1%91%D1%80%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE
"""

from tree_interface import TreeInterface
from enum import IntEnum, auto, unique


class ResBlackTree(TreeInterface):

    @unique
    class Color(IntEnum):
        RED = auto()
        BLACK = auto()

    class Node:
        def __init__(self, value: int) -> None:
            super().__init__()
            self.value: int = value
            self.left: ResBlackTree.Node = None
            self.right: ResBlackTree.Node = None
            self.parent: ResBlackTree.Node = None
            self.color: ResBlackTree.Color = ResBlackTree.Color.BLACK

        def __repr__(self) -> str:
            return str(self.value)

    def __init__(self) -> None:
        super().__init__()
        self.root: ResBlackTree.Node = None

    def __get_grandparent(self, node: Node) -> Node:
        if node is None or node.parent is None:
            return None
        else:
            return node.parent.parent

    def __get_uncle(self, node: Node) -> Node:
        gtandparent: ResBlackTree.Node = self.__get_grandparent(node)
        if not gtandparent:
            return None
        if node.parent == gtandparent.left:
            return gtandparent.right
        else:
            return gtandparent.left

"""
Реализация красно-черного дерева
За основу взят пример отсюда: http://algolist.ru/ds/rbtree.php
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

    
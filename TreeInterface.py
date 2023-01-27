from abc import ABC, abstractmethod

class TreeInterface(ABC):
    @abstractmethod
    def insert(item):
        pass

    @abstractmethod
    def remove(item):
        pass

    @abstractmethod
    def contains(item) -> bool:
        pass
"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.data = dict()  # todo для очереди можно использовать python dict

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        if priority in self.data:
            self.data[priority].insert(0, elem)
        else:
            self.data[priority] = [elem]
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        return None

    def dequeue(self) -> Any:
        for i in self.data:
            print(i)
            if self.data[i]:
                print(i)
                return self.data[i].pop()
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        return None

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        if self.data[priority]:
            return self.data[priority][-1 - ind]
        return None

    def clear(self) -> None:
        self.data.clear()
        """
        Clear my queue

        :return: None
        """
        return None

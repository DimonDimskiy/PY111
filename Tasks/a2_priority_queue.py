"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:

    def __init__(self, priorities: int = 10):
        self._priorities = priorities
        self.data = {i: [] for i in range(self._priorities + 1)}  # todo для очереди можно использовать python dict

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :param priority: elements priority
        :return: Nothing
        """
        self.data[priority].append(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        for i in range(self._priorities + 1):
            if self.data[i]:
                return self.data[i].pop(0)


    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if priority in self.data:
            if ind < len(self.data[priority]):
                return self.data[priority][ind]
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        for i in self.data:
            self.data[i].clear()
        return None

if __name__ == "__main__":
    my_q = PriorityQueue()
    my_q.enqueue(1)
    my_q.enqueue(2)
    print(my_q.data)
    print(my_q.dequeue())
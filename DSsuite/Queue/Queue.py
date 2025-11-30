from DSsuite.LinkedList.linkedList import LinkedList
from DSsuite.LinkedList.LinkedListIterator import LinkedListIterator

class Queue:
    def __init__(self):
        self._queue = LinkedList()

    def enqueue(self,value):
        self._queue.append(value)

    def dequeue(self):
        try:
            return self._queue.remove(0)
        except IndexError:
            raise IndexError("Dequeue at empty queue")

    def front(self):
        try:
            return self._queue[0]
        except IndexError:
            raise IndexError("Peek in empty queue")

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        if len(self._queue):
            return False
        return True

    def __iter__(self):
        return LinkedListIterator(self._queue)

    def __repr__(self):
        queue = [x for x in self]

        return "Queue["+",".join([str(x) for x in queue])+"]"



from DSsuite.LinkedList.linkedList import LinkedList
from DSsuite.LinkedList.LinkedListIterator import LinkedListIterator
class Stack:
    def __init__(self):
        self._stack = LinkedList()

    def push(self,data):
        try:
            self._stack.prepend(data)
        except Exception:
            raise Exception("Implementation Error")

    def pop(self):
        try:
            return self._stack.remove(0)
        except IndexError:
            raise IndexError("Pop from empty stack")

    def peek(self):
        try:
            return self._stack[0]
        except IndexError:
            raise IndexError("Peek in an empty stack")

    def __len__(self):
        return len(self._stack)

    def is_empty(self):
        if len(self._stack):
            return False
        return True

    def __iter__(self):
        return LinkedListIterator(self._stack)

    def __repr__(self):
        stack = []
        for x in self:
            stack.append(x)
        return "stack["+",".join([str(x) for x in stack])+"]"


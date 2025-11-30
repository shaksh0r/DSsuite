class LinkedListIterator:
    def __init__(self,ll):
        self.current = ll.get_head()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current.next is not None:
            self.current = self.current.next
            return self.current.data
        else:
            raise StopIteration
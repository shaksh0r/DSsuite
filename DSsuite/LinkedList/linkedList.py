from DSsuite.Node.Node import Node
from DSsuite.LinkedList.LinkedListIterator import LinkedListIterator
class LinkedList:
    def __init__(self,initial_list=None):
        self.head = Node(None,None,None)
        self.tail = self.head
        self.length = 0
        self.build_list(initial_list)

    def build_list(self,initial_list):
        if initial_list is not None:
            for index,item in enumerate(initial_list):
                self.append(item)

    @staticmethod
    def create_node(data,next_node,prev_node):
        return Node(data,next_node,prev_node)

    def prepend(self,data):
        temp = LinkedList.create_node(data,None,None)
        temp.next = self.head.next
        temp.prev = self.head
        if self.head.next is not None:
            self.head.next.prev = temp
        else:
            self.tail = temp
        self.head.next = temp
        self.length += 1

    def append(self,data):
        temp = LinkedList.create_node(data,None,None)
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        self.length += 1

    # def insert_at(self,data,position):
    #     curr = self.head
    #     node = LinkedList.create_node(data,None)
    #     i = 0
    #     while curr.next is not None:
    #         if i == position:
    #             temp = curr.next
    #             curr.next = node
    #             node.next = temp
    #             return None
    #         else:
    #             curr = curr.next
    #             i += 1
    #     raise IndexError("Index Out of Bounds")

    def __setitem__(self, key, value):
        curr = self.head.next
        node = LinkedList.create_node(value,None,None)
        i = 0
        while curr is not None:
            if i == key:
                curr.prev.next = node
                node.next = curr.next
                node.prev = curr.prev
                if key == self.length - 1:
                    self.tail = node
                    return None
                return None
            else:
                i += 1
                curr = curr.next
        raise IndexError("Index Out of Bounds")

    def get_head(self):
        return self.head

    def __reversed__(self):
        current = self.tail
        while current is not None and current is not self.head:
            yield current.data
            current = current.prev


    def remove(self,position):
        curr = self.head.next
        i = 0
        while curr is not None:
            data = curr.data
            if i == position:
                curr.prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                if position == self.length - 1:
                    self.tail = curr.prev
                self.length -= 1
                return data
            else:
                curr = curr.next
                i += 1
        raise IndexError("Not Found")

    def show_all(self):
        print("The Linked List:")
        print("=>=>=>=>=>=>=>=>")
        point = self.head.next

        while point is not None:
            print(point.data)
            point = point.next

    def __iter__(self):
        return LinkedListIterator(self)


    def __getitem__(self, item):
        point = self.head.next
        i = 0
        while point is not None:
            if i == item :
                return point.data
            point = point.next
            i += 1
        raise IndexError

    def __len__(self):
        return self.length



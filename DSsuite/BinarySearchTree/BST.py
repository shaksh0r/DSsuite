from DSsuite.BinarySearchTree.Node import Node

class BST:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self,key,value=None):
        node = Node(key,value)
        if self.root is None:
            self.root = node
            self.length += 1
        else:
            curr = self.root
            while True:
                if key > curr.key:
                    if curr.right is None:
                        curr.right = node
                        self.length += 1
                        return
                    else:
                        curr = curr.right
                else:
                    if curr.left is None:
                        curr.left = node
                        self.length += 1
                        return
                    else:
                        curr = curr.left

    def find(self,key):
        curr = self.root
        while curr is not None:
            if key == curr.key:
                return curr
            elif key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left

        raise KeyError("Key not found")

    def __contains__(self, key):
        curr = self.root
        while curr is not None:
            if key == curr.key:
                return True
            elif key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left

        return False

    def __len__(self):
        return self.length

    def remove(self, key):
        parent = None
        curr = self.root

        while curr is not None:
            if key == curr.key:
                break
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            raise KeyError("Key not found")

        if curr.left is None or curr.right is None:
            child = curr.left if curr.left is not None else curr.right

            if parent is None:
                self.root = child
            else:
                if parent.left is curr:
                    parent.left = child
                else:
                    parent.right = child

            self.length -= 1
            return

        pred_parent = curr
        pred = curr.left

        while pred.right is not None:
            pred_parent = pred
            pred = pred.right


        if pred_parent is curr:
            pred_parent.left = pred.left
        else:
            pred_parent.right = pred.left

        curr.key = pred.key
        curr.data = pred.data

        self.length -= 1

    def __iter__(self):
        return self.in_order()

    def min(self):
        curr = self.root
        while curr.left is not None:
            curr = curr.left

        return curr

    def max(self):
        curr = self.root
        while curr.right is not None:
            curr = curr.right

        return curr

    def print_tree(self,curr):
        if curr is None:
            return
        print(curr.key)
        self.print_tree(curr.left)
        self.print_tree(curr.right)

    def in_order(self):
        yield from self._in_order(self.root)

    def _in_order(self,curr):
        if curr is None:
            return
        yield from self._in_order(curr.left)
        yield curr.key
        yield from self._in_order(curr.right)

    def items(self):
        yield from self._items(self.root)

    def _items(self,curr):
        if curr is None:
            return
        yield from self._items(curr.left)
        yield curr.key,curr.data
        yield from self._items(curr.right)

    def keys(self):
        yield from self._keys(self.root)

    def _keys(self,curr):
        if curr is None:
            return
        yield from self._keys(curr.left)
        yield curr.key
        yield from self._keys(curr.right)

    def values(self):
        yield from self._values(self.root)

    def _values(self,curr):
        if curr is None:
            return
        yield from self._values(curr.left)
        yield curr.data
        yield from self._values(curr.right)

    def heights(self):
        yield from self._heights(self.root)

    def _heights(self,curr):
        if curr is None:
            return 0

        return 1 + max(self._heights(curr.left),self._heights(curr.right))

    def is_empty(self):
        return True if self.length == 0 else False




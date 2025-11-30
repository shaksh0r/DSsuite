class BSTIterator:
    def __init__(self,BST):
        self.curr = BST.root

    def __iter__(self):
        return self

    def __next__(self):

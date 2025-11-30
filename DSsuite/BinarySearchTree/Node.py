class Node:
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.key,self.data})"
    
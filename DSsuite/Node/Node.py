class Node:
    def __init__(self,data,next_node=None,prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node
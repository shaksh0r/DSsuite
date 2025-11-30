from Queue import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())   # 1
q.enqueue(3)
q.enqueue(4)
print(list(q))       # Expected: [2, 3, 4]
q.dequeue()
print(q.front())     # Expected: 3

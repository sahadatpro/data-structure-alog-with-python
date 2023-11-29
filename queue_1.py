# Queue - Datastucture.
"""
=> Basic Opertion of queue.
    -> Enqueue.
    -> Dequeue.
    -> isEmpty.
    ->isFull.
    -> Peek 
"""
#Eample simple Queue
class Queue():
    def __init__(self):
        self.data = []

    # Add element
    def enqueue(self, item):
        self.data.append(item)
    # Remove element
    def dequeue(self):
        if len(self.data) < 1:
            return None
        return self.data.pop(0)
    # Display the queue
    def display(self):
        print(self.data)

    # Size the queue
    def size(self):
        print(len(self.data))


# Queue exicutation 
q = Queue()
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.enqueue(80)
q.enqueue(90)

q.size()
q.display()
q.dequeue()
q.dequeue()
q.display();

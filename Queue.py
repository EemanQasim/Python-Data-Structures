
'''Creating a Queue class in Python using a list '''

class Queue:

    def __init__(self):
       self.items = [] 

    def enqueue(self,item):
        '''Adds an item to the back of the queue'''
        self.items.insert(0,item) 

    def dequeue(self):
        '''Returns and removes the item in the front of the queue'''
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        '''shows the item at the front of the queue'''
        if self.items:
            return self.items[-1]
        return None 

    def size(self):
        '''Returns the size of the queue'''
        return len(self.items)

    def is_empty(self):
        '''Returns a boolean value whether the queue is empty or not'''
        return self.items == []



my_q = Queue()

my_q.enqueue('apple')
print(my_q.items)
my_q.enqueue('banana')
print(my_q.items)
my_q.dequeue()
print(my_q.items)
print(my_q.peek())
print(my_q.size())
print(my_q.is_empty())

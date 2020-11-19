
'''Creating a Stack in Python by using a list'''

class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        '''Appends item to end of list'''
        self.items.append(item)

    def pop(self):
        '''Returns and removes items at front of the Stack'''
        self.items.pop()

        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        '''Shows the next item to be removed'''
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        '''Returns the size of the Stack'''
        return len(self.items)


    def is_empty(self):
        '''Returns a Boolean showing if Stack is empty or not'''
        return self.items == []



mystack = Stack()

mystack.push('apple')
print(mystack.items)
mystack.push('banana')
print(mystack.items)
# # mystack.push('carrot')
# print(mystack.items)
# print(mystack.pop())
# print(mystack.items)
# mystack.peek()
print(mystack.size())
print(mystack.peek())
print(mystack.is_empty())
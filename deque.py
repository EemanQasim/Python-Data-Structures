
'''Creating a Deque Class in Python by using a class'''


class Deque:

    def __init__(self):
        self.items = []

    def add_front(self , item):
        '''Left side as the front of the list zero index '''
        self.items.insert(0,item)


    def add_rear(self, item):
        '''the right side of the list -1 index'''
        self.items.append(item)


    def remove_front(self):
        '''Removes Value found at index 0'''
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        '''Removes Value found at index -1'''
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        '''Returns Value found at index 0'''
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        '''Returns Value found at index -1'''
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        '''Returns the length of items'''
        if self.items:
            return len(self.items)
        return None

    def is_empty(self):
        return self.items == []


my_D = Deque()

my_D.add_front('Front')
my_D.add_rear('Rear')
print(my_D.items)
my_D.add_front('Another Front')
print(my_D.items)

# my_D.remove_front()
# print(my_D.items)
# my_D.remove_rear()
# print(my_D.items)

print(my_D.peek_front())
print(my_D.peek_rear())
print(my_D.size())
print(my_D.is_empty())

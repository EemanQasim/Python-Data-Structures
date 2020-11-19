

'''Palindrome Checker'''


class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        '''Left side as the front of the list zero index '''
        self.items.insert(0, item)

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
        '''Returns a Boolean Value showing if items is empty or not'''
        return self.items == []


def check_palindrome(input_str):
        my_d = Deque()
        for char in input_str:
            my_d.add_rear(char)

        while my_d.size() >=2:
            front_item = my_d.remove_front()
            rear_item = my_d.remove_rear()

            if front_item != rear_item:
                return False 
        return True


print(check_palindrome('racecar'))
print(check_palindrome('oranges'))



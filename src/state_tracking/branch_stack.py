
class BranchStack(object):
    '''Stack that stores and manages all the context branches'''

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise EmptyStackError()
        return self.items.pop()

    def peek_top(self):
        '''Return the top item on the stack'''
        return self.items[len(self.items)-1]

    def peek_second(self):
        '''Return the second item on the stack'''
        return self.items[len(self.items)-2]

    def size(self):
        return len(self.items)

    def replace(self, item):
        '''Replace the top item on the stack'''
        self.pop()
        self.push(item)
    
    def empty_stack(self):
        self.items = []
    
    def print_stack(self):
        print(self.items)

    
class EmptyStackError(Exception):
        def __init__(self):
                super().__init__("Stack is empty: cannot pop from an empty stack!")
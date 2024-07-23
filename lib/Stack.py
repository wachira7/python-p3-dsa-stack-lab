class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def __str__(self):
        return str(self.items)
        
    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.limit

    def push(self, item):
        if not self.isFull():
            self.items.append(item)
        else:
            print("Stack is full.")


    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty.")

    
    def size(self):
        return len(self.items)

    
    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return self.items[::-1].index(target)
        else:
            return -1
        







# For my reference:

"""line self.items[::-1].index(target):

self.items[::-1]:

This part of the code reverses the list self.items.

The slicing notation [::-1] means "take the list and return a new list that is a reversed version of the original."
For example, if self.items is [5, 6, 7, 8, 9, 10], then self.items[::-1] would be [10, 9, 8, 7, 6, 5].
.index(target):

This part of the code finds the index of the target element in the reversed list.
The .index() method returns the first index at which a specified value is found.
For example, if the target is 5 in the reversed list [10, 9, 8, 7, 6, 5], the .index(5) method would return 5 because 5 is at the 5th index in the reversed list.
Combining these two parts:

self.items[::-1] creates a reversed version of the stack.
.index(target) finds the index of the target element in this reversed list.
This effectively gives the position of the target element when viewed from the top of the stack (where the last element of the original list is considered the top of the stack)."""

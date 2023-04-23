from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def push(self, value):
        self.q1.put(value)
    
    def pop(self):
        if self.q1.empty():
            return None
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        result = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self):
        if self.q1.empty():
            return None
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        result = self.q1.get()
        self.q2.put(result)
        self.q1, self.q2 = self.q2, self.q1
        return result

    def is_empty(self):
        return self.q1.empty()

# Example usage of the stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())    # prints 3
print(stack.top())    # prints 2
print(stack.is_empty())    # prints False

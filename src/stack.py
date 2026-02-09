from src.errors import STACK_UNDERFLOW

class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.data:
            raise Exception(STACK_UNDERFLOW)
        return self.data.pop()
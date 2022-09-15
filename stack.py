from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def is_balanced(self, str):
        for element in str:
            if element == "[" or element == "(":
                self.push(element)
            if element == "]":
                if self.is_empty() or self.peek() != "[":
                    return False
                else:
                    self.pop()

            if element == ")":
                if self.is_empty() or self.peek() != "(":
                    return False
                else:
                    self.pop()
        return True


s = Stack()
print(s.is_balanced("(](a+b)[()]"))

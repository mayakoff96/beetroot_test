class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

    def get_from_stack(self, element):
        temp_stack = Stack()
        found = False

        while not self.is_empty():
            item = self.pop()
            if item == element:
                found = True
                break
            temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the stack")


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.get_from_stack(3))
print(s.get_from_stack(1))

try:
    print(s.get_from_stack(6))
except ValueError as e:
    print(str(e))

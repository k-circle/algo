class Stack:
    def __init__(self, size):
        self._size = size
        self._stack = []

    def push(self, item):
        if len(self._stack) >= self._size:
            print('stack overflow')
            return
        self._stack.append(item)

    def pop(self):
        if len(self._stack) <= 0:
            print('stack underflow')
            return
        return self._stack.pop()

    def top(self):
        if not self._stack:
            return None
        return self._stack[-1]

    def empty(self):
        self._stack.clear()

    def size(self):
        print(len(self._stack))


if __name__ == '__main__':
    s = Stack(3)
    s.push("a")
    s.push("b")
    s.push("c")
    s.push("d")  # overflow
    print(s.pop())  # c
    print(s.pop())  # b
    print(s.pop())  # a
    s.pop()  # underflow
    s.size()  # 0
    s.push("A")
    s.size()  # 1
    s.empty()
    s.size()  # 0

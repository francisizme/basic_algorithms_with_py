class Stack:
    def __init__(self):
        self.__stack = []

    def append(self, value: any):
        self.__stack.append(value)

    def pop(self):
        self.__stack = self.__stack[:-1]

    def peek(self):
        return self.__stack[-1] if len(self.__stack) else None



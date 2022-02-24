class _Node:
    def __init__(self, value, next_node=None):
        self.__value = value
        self.__next_node = next_node

    def get_value(self):
        return self.__value

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, next_node):
        self.__next_node = next_node


class Stack:
    def __init__(self, limit=1000):
        self.__top_item = None
        self.__limit = limit
        self.__size = 0

    def peek(self):
        if not self.is_empty():
            return self.__top_item.get_value()
        print('The stack is empty!')

    def push(self, value):
        if self.has_space():
            item = _Node(value)
            item.set_next_node(self.__top_item)
            self.__top_item = item
            self.__size += 1
        else:
            print('All out of space!')

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.__top_item
            self.__top_item = item_to_remove.get_next_node()
            self.__size -= 1
            return item_to_remove.get_value()
        print('The stack is empty!')

    def has_space(self):
        return self.__size < self.__limit

    def is_empty(self):
        return self.__size == 0


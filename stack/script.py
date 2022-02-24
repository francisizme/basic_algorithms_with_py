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
    def __init__(self, **kwargs):
        self.__top_item = None
        self.__size = 0
        self.__limit = kwargs.get('limit', 1000)
        self.__name = kwargs.get('name', None)

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

    def get_name(self):
        return self.__name

    def has_space(self):
        return self.__size < self.__limit

    def is_empty(self):
        return self.__size == 0

    def get_size(self):
        return self.__size

    def print_items(self):
        pointer = self.__top_item
        print_list = []
        while pointer:
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))


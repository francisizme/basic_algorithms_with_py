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


class Queue:
    def __init__(self, max_size=None):
        self.__head = None
        self.__tail = None
        self.__max_size = max_size
        self.__size = 0

    def peek(self):
        if self.is_empty():
            print('Nothing to see here!')
        else:
            return self.__head.get_value()

    def get_size(self):
        return self.__size

    def has_space(self):
        return self.__max_size > self.__size if self.__max_size is not None else True

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, value):
        if self.has_space():
            print(f'Adding {str(value)} to the queue!')
            item_to_add = _Node(value)
            if self.is_empty():
                self.__head = item_to_add
            else:
                self.__head.set_next_node(item_to_add)
            self.__tail = item_to_add
            self.__size += 1
        else:
            print('Sorry, no more room!')

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.__head
            print(f'Removing {str(item_to_remove.get_value())} from the queue!')
            if self.__size == 1:
                self.__head = None
                self.__tail = None
            else:
                self.__head = item_to_remove.get_next_node()
            self.__size -= 1
            return item_to_remove.get_value()
        else:
            print('This queue is totally empty!')

class BinaryTree:
    def __init__(self, value, depth=1):
        self.__value = value
        self.__depth = depth
        self.__duplicate = 1
        self.__left = None
        self.__right = None

    def get_value(self):
        return self.__value

    def get_depth(self):
        return self.__depth

    def count(self):
        return self.__duplicate

    def insert(self, value):
        if value == self.__value:
            self.__duplicate += 1
        if value > self.__value:
            if self.__right:
                self.__right.insert(value)
            else:
                self.__right = BinaryTree(value, self.__depth + 1)
        if value < self.__value:
            if self.__left:
                self.__left.insert(value)
            else:
                self.__left = BinaryTree(value, self.__depth + 1)

    def find_node_by_value(self, value):
        if self.__value == value:
            return self
        if value < self.__value and self.__left:
            return self.__left.find_node_by_value(value)
        if value > self.__value and self.__right:
            return self.__right.find_node_by_value(value)
        return 'value not found'

    def traverse(self):
        if self.__left:
            self.__left.traverse()
        print(self.__value)
        if self.__right:
            self.__right.traverse()

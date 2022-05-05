class BinaryTree:
    def __init__(self, value, depth=1):
        self._value = value
        self._depth = depth
        self._duplicate = 1
        self._left = None
        self._right = None

    def get_value(self):
        return self._value

    def get_depth(self):
        return self._depth

    def count(self):
        return self._duplicate

    def insert(self, value):
        if value == self._value:
            self._duplicate += 1
        if value > self._value:
            if self._right:
                self._right.insert(value)
            else:
                self._right = BinaryTree(value, self._depth + 1)
        if value < self._value:
            if self._left:
                self._left.insert(value)
            else:
                self._left = BinaryTree(value, self._depth + 1)

    def find_node_by_value(self, value):
        if self._value == value:
            return self
        if value < self._value and self._left:
            return self._left.find_node_by_value(value)
        if value > self._value and self._right:
            return self._right.find_node_by_value(value)
        return 'value not found'

    def traverse(self):
        if self._left:
            self._left.traverse()
        print(self._value)
        if self._right:
            self._right.traverse()

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


class LinkedList:
    def __init__(self, value=None):
        self.__head_node = _Node(value)

    def get_head_node(self):
        return self.__head_node

    def insert_beginning(self, new_value):
        new_node = _Node(new_value)
        new_node.set_next_node(self.__head_node)
        self.__head_node = new_node

    def stringify_list(self):
        str_list = []
        current_node = self.__head_node
        while current_node:
            str_list.append(current_node.get_value())
            if current_node.get_next_node() is None:
                return '\n'.join(map(str, str_list))
            current_node = current_node.get_next_node()

    def remove_node(self, value_to_remove):
        current_node = self.__head_node
        if current_node.get_value() == value_to_remove:
            self.__head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    self.__head_node = next_node.get_next_node()
                    current_node = None
                else:
                    current_node = next_node

    def swap_node(self, val1, val2):
        print(f'Swapping node {val1} and {val2}')

        if val1 == val2:
            raise ValueError(f'Cannot swap the same nodes')

        node1_prev = None
        node2_prev = None
        node1 = self.__head_node
        node2 = self.__head_node

        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if node1 is None or node2 is None:
            raise ValueError(f'Cannot swap node {val1} and {val2}')

        if node1_prev is None:
            self.__head_node = node2
        else:
            node1_prev.set_next_node(node2)
        if node2_prev is None:
            self.__head_node = node1
        else:
            node2_prev.set_next_node(node1)

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)

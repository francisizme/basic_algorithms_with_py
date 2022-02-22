class Node:
    def __init__(self, value, link_node=None):
        self.__value = value
        self.__link_node = link_node

    def get_value(self):
        return self.__value

    def get_link_node(self):
        return self.__link_node

    def set_link_node(self, link_node):
        self.__link_node = link_node

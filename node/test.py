import unittest
from script import Node


class NodeTestCase(unittest.TestCase):
    def test_node(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        self.assertEqual(node1.get_value(), 1)
        node1.set_link_node(node2)
        self.assertEqual(node1.get_link_node().get_value(), 2)
        node2.set_link_node(node3)
        self.assertEqual(node2.get_link_node().get_value(), 3)
        node1.set_link_node(node3)
        self.assertEqual(node1.get_link_node().get_value(), 3)


if __name__ == '__main__':
    unittest.main()

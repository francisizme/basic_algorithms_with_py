import unittest

from script import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def test_linked_list(self):
        ll = LinkedList('My')
        ll.insert_beginning('name')
        ll.insert_beginning('is')
        ll.insert_beginning('Francis')
        self.assertEqual(ll.get_head_node().get_value(), 'Francis')
        self.assertEqual(ll.stringify_list(), '\n'.join(['Francis', 'is', 'name', 'My']))
        ll.swap_node('Francis', 'My')
        ll.swap_node('is', 'name')
        self.assertEqual(ll.stringify_list(), '\n'.join(['My', 'name', 'is', 'Francis']))
        ll.remove_node('My')
        self.assertEqual(ll.stringify_list(), '\n'.join(['name', 'is', 'Francis']))
        ll.remove_node('is')
        self.assertEqual(ll.stringify_list(), 'Francis')


if __name__ == '__main__':
    unittest.main()

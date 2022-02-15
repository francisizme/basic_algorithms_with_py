import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    def test_stack(self):
        my_stack = Stack()
        self.assertIsNone(my_stack.peek())
        my_stack.append(1)
        self.assertEqual(my_stack.peek(), 1)
        my_stack.append(2)
        self.assertEqual(my_stack.peek(), 2)
        my_stack.pop()
        self.assertEqual(my_stack.peek(), 1)
        my_stack.pop()
        self.assertIsNone(my_stack.peek())


if __name__ == '__main__':
    unittest.main()

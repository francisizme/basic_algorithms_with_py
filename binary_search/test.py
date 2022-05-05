from script import binary_search_recursive, binary_search_pointers
from bst import BinaryTree
import io
import sys


def test_binary_search_recursive():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search_recursive(input_list, 0) == 'value not found'
    assert binary_search_recursive(input_list, 2) == 1
    assert binary_search_recursive(input_list, 7) == 6


def test_binary_search_pointers():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search_pointers(input_list, 0) == 'value not found'
    assert binary_search_pointers(input_list, 2) == 1
    assert binary_search_pointers(input_list, 7) == 6


def test_binary_tree():
    bst = BinaryTree(5)
    bst.insert(7)
    bst.insert(1)
    bst.insert(6)
    bst.insert(9)
    bst.insert(6)

    assert bst.find_node_by_value(10) == 'value not found'
    assert bst.find_node_by_value(6).get_value() == 6
    assert bst.find_node_by_value(6).get_depth() == 3
    assert bst.find_node_by_value(6).count() == 2
    captured_output = io.StringIO()
    sys.stdout = captured_output
    bst.traverse()
    assert captured_output.getvalue().strip() == '\n'.join(map(str, [1, 5, 6, 7, 9]))
    sys.stdout = sys.__stdout__

import pytest
import io
import sys
from script import naive_pattern


def test_search():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    naive_pattern('Hello World', 'o')
    naive_pattern('Hello World', 'O')
    assert captured_output.getvalue().strip() == 'o is found at index 4\no is found at index 7\nO is found at index 4\nO is found at index 7'
    sys.stdout = sys.__stdout__

def test_search_sensitive():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    naive_pattern('Hello World', 'o')
    naive_pattern('Hello World', 'O', sensitive=True)
    assert captured_output.getvalue().strip() == 'o is found at index 4\no is found at index 7'
    sys.stdout = sys.__stdout__

def test_search_and_replace():
    assert naive_pattern('Hello World', 'o', replacement='a') == 'Hella Warld'

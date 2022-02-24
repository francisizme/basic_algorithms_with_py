import pytest
import io
import sys
from script import Stack


def test_create_stack():
    s = Stack()
    assert s is not None


@pytest.fixture()
def empty_s():
    return Stack()


@pytest.fixture()
def limit_s():
   return Stack(1)


@pytest.fixture()
def full_s():
    s = Stack(1)
    s.push(1)
    return s


def test_peek(empty_s, full_s):
    assert full_s.peek() == 1

    captured_output = io.StringIO()
    sys.stdout = captured_output
    empty_s.peek()
    assert captured_output.getvalue().strip() == 'The stack is empty!'
    sys.stdout = sys.__stdout__


def test_push(empty_s, limit_s, full_s):
    assert empty_s.is_empty() is True
    empty_s.push(1)
    assert empty_s.is_empty() is False

    assert limit_s.has_space() is True
    limit_s.push(1)
    assert limit_s.has_space() is False

    assert full_s.has_space() is False
    captured_output = io.StringIO()
    sys.stdout = captured_output
    full_s.push(1)
    assert captured_output.getvalue().strip() == 'All out of space!'
    sys.stdout = sys.__stdout__


def test_pop(full_s):
    assert full_s.peek() == 1
    assert full_s.pop() == 1
    captured_output = io.StringIO()
    sys.stdout = captured_output
    full_s.pop()
    assert captured_output.getvalue().strip() == 'The stack is empty!'
    sys.stdout = sys.__stdout__

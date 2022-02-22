import pytest
import io
import sys
from script import Queue


def test_create_queue():
    un_limit_q = Queue()
    limit_q = Queue(1)
    assert un_limit_q is not None
    assert limit_q is not None


@pytest.fixture()
def limit_q():
    queue = Queue(3)
    queue.enqueue('My')
    return queue


@pytest.fixture()
def un_limit_q():
    queue = Queue()
    queue.enqueue('My')
    return queue


def test_enqueue(limit_q, un_limit_q):
    limit_q.enqueue('name')
    limit_q.enqueue('is')
    assert limit_q.has_space() is False
    un_limit_q.enqueue('name')
    un_limit_q.enqueue('is')
    un_limit_q.enqueue('Francis')
    assert un_limit_q.has_space() is True

    captured_output = io.StringIO()
    sys.stdout = captured_output
    limit_q.enqueue('Francis')
    assert captured_output.getvalue().strip() == 'Sorry, no more room!'
    sys.stdout = sys.__stdout__


def test_dequeue(limit_q):
    limit_q.enqueue('name')
    assert limit_q.dequeue() == 'My'
    assert limit_q.dequeue() == 'name'
    assert limit_q.is_empty() is True

    captured_output = io.StringIO()
    sys.stdout = captured_output
    limit_q.dequeue()
    assert captured_output.getvalue().strip() == 'This queue is totally empty!'
    sys.stdout = sys.__stdout__


def test_peek(limit_q):
    assert limit_q.peek() == 'My'
    limit_q.enqueue('name')
    assert limit_q.peek() == 'My'

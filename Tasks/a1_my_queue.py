"""
My little Queue
"""
from typing import Any
queue_ = []

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global queue_
    queue_.append(elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    global queue_
    if queue_:
        return queue_.pop(0)
    return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global queue_
    if queue_:
        if 0 <= ind < len(queue_):
            return queue_[ind]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global queue_
    queue_.clear()

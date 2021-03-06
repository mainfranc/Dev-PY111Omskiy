"""
My little Stack
"""
from typing import Any
stack_ = []

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    global stack_
    stack_.append(elem)
    # some another change
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.
    :return: popped element
    """
    global stack_
    if not stack_:
        return None
    return stack_.pop(len(stack_) - 1)


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    global stack_
    if 0 <= ind < len(stack_):
        return stack_[len(stack_) - 1 - ind]
    return None


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global stack_
    stack_.clear()
    return None

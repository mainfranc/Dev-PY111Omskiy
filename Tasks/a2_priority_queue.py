"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
prior_queue = []

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global prior_queue
    prior_queue.append([elem, priority])


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global prior_queue
    if prior_queue:
        priorities_set = set()
        for i in prior_queue:
            priorities_set.add(i[1])
        max_priority = min(priorities_set)
        for i in range(len(prior_queue)):
            if prior_queue[i][1] == max_priority:
                el_to_return =  prior_queue[i][0]
                prior_queue.pop(i)
                return el_to_return
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global prior_queue
    if prior_queue:
        curr_prior = []
        for i in range(len(prior_queue)):
            if priority == prior_queue[i][1]:
                curr_prior.append([prior_queue[i][0], i])
        if curr_prior:
            if 0 <= ind < len(curr_prior):
                return curr_prior[ind][0]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global prior_queue
    prior_queue.clear()


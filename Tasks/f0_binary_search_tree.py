"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx
ex_tree = {}

def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global ex_tree
    if not ex_tree:
        ex_tree = {"key": key, "value": value, "left": {}, "right": {}}
        return None

    curr_node = ex_tree
    while curr_node:
        if curr_node['key'] == key:
            curr_node['value'] = value
            return None
        elif curr_node['key'] > key:
            if not curr_node['left']:
                curr_node['left'] = {"key": key, "value": value, "left": {}, "right": {}}
                return None
            else:
                curr_node = curr_node['left']
        else:
            if not curr_node['right']:
                curr_node['right'] = {"key": key, "value": value, "left": {}, "right": {}}
                return None
            else:
                curr_node = curr_node['right']
    return None


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    global ex_tree
    try:
        find(key)
    except KeyError:
        return None

    curr_node = ex_tree
    parent_node = {}
    while curr_node:
        if curr_node['key'] == key:
            break
        elif curr_node['key'] < key:
            parent_node = curr_node
            curr_node = curr_node['right']
        else:
            parent_node = curr_node
            curr_node = curr_node['left']

    result = (curr_node['key'], curr_node['value'])
    if not any((curr_node['left'], curr_node['right'])):
        curr_node = {}
    else:
        if not all((curr_node['left'], curr_node['right'])):
            dir = 'left' if curr_node['left'] else 'right'
            curr_node = curr_node[dir]
        else:
            new_min_in_right = curr_node['right']
            while new_min_in_right['left']:
                new_min_in_right = new_min_in_right['left']
            new_key_val = remove(new_min_in_right['key'])
            curr_node['key'] = new_key_val[0]
            curr_node['value'] = new_key_val[1]
    return result


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    curr_node = ex_tree
    while curr_node:
        if curr_node['key'] == key:
            return curr_node['value']
        elif curr_node['key'] < key:
            curr_node = curr_node['right']
        else:
            curr_node = curr_node['left']
    raise KeyError("key not found")


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    ex_tree.clear()
    return None


if __name__ == '__main__':
    ex_tree = {'key': 42,
               'value': 'some val',
               'left': {
                   'key': 21,
                   'value': 'some val2',
                   'left': {
                       'key': 12,
                       'value': 'some val3',
                       'left': {

                       },
                       'right': {

                       }
                   },
                   'right': {

                   }
               },
               'right': {
                   'key': 64,
                   'value': 'some val4',
                   'left': {
                       'key': 56,
                       'value': 'some val5',
                       'left': {

                       },
                       'right': {

                       }
                   },
                   'right': {
                       'key': 78,
                       'value': 'some val6',
                       'left': {

                       },
                       'right': {

                       }
                   }
               }
               }
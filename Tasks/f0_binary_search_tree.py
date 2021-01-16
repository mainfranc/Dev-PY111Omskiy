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
    result = None

    curr_node = return_node(key)
    if not curr_node: return None

    if not any((curr_node['left'], curr_node['right'])):
        result = (curr_node['key'], curr_node['value'])
        curr_node = {}
    else:
        if not all((curr_node['left'], curr_node['right'])):
            result = (curr_node['key'], curr_node['value'])
            dir_ = 'left' if curr_node['left'] else 'right'
            curr_node = curr_node[dir_]
        else:
            result = (curr_node['key'], curr_node['value'])
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
    curr_node = return_node(key)
    if curr_node:
        return curr_node['value']
    else:
        raise KeyError("key not found")


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    ex_tree.clear()
    return None


def return_node(key):
    curr_node = ex_tree
    while curr_node:
        if curr_node['key'] == key:
            return curr_node
        elif curr_node['key'] < key:
            curr_node = curr_node['right']
        else:
            curr_node = curr_node['left']

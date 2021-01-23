from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: substring for prefix function
    :return: prefix values table
    """
    result = [0 for i in range(len(prefix_str))]
    for i in range(1, len(prefix_str) + 1):
        addition = [j if prefix_str[:j] == prefix_str[i - j:i] else 0 for j in range(1, i)]
        if addition: result[i - 1] = max(addition)
    return result


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    lst_mapping = _prefix_fun(substr)
    inp_i = 0

    while inp_i < len(inp_string):
        for sub_i in range(len(substr)):
            if inp_string[inp_i + sub_i] == substr[sub_i]:
                if sub_i == len(substr) - 1:
                    return inp_i
            else:
                inp_i -= lst_mapping[sub_i]
                break
        inp_i += 1
    print(inp_string, substr, _prefix_fun)
    return None


if __name__ == '__main__':
    print(_prefix_fun('abcabca'))


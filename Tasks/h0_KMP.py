from typing import Optional, List
import timeit


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
    return None


if __name__ == '__main__':
    setup = """
str_to_test = '22 января 1991 года в СССР началась «павловская» денежная реформа. Названа она была так в честь инициатора – премьер-министра Валентина Павлова. Хотя распоряжение Павлова предварялось его собственными публичными заверениями, что денежная реформа проводиться не будет.'


def _prefix_fun(prefix_str):
    result = [0 for i in range(len(prefix_str))]
    for i in range(1, len(prefix_str) + 1):
        addition = [j if compare_string_parts(prefix_str, j, i - j) else 0 for j in range(1, i)]
        if addition: result[i - 1] = max(addition)
    return result
    
    
def _prefix_fun_slice(prefix_str):
    result = [0 for i in range(len(prefix_str))]
    for i in range(1, len(prefix_str) + 1):
        addition = [j if prefix_str[:j] == prefix_str[i - j:i] else 0 for j in range(1, i)]
        if addition: result[i - 1] = max(addition)
    return result


def _prefix_fun2(prefix_str):
    P = [0] * len(prefix_str)
    j = 0
    i = 1

    while i < len(prefix_str):
        if prefix_str[j] != prefix_str[i]:
            if j > 0:
                j = P[j - 1]
            else:  # j == 0
                i += 1
        else:
            P[i] = j + 1
            i += 1
            j += 1
    return P

def compare_string_parts(in_str, i2, j1):
    marker = True
    for i in range(i2):
        if in_str[i] != in_str[j1 + i]:
            marker = False
    return marker
    """
    print(min(timeit.Timer('_prefix_fun("abcabca")', setup).repeat(1, 10)))
    print(min(timeit.Timer('_prefix_fun2("abcabca")', setup).repeat(1, 10)))
    print(min(timeit.Timer('_prefix_fun_slice("abcabca")', setup).repeat(1, 10)))

    print(min(timeit.Timer('_prefix_fun(str_to_test)', setup).repeat(1, 10)))
    print(min(timeit.Timer('_prefix_fun2(str_to_test)', setup).repeat(1, 10)))
    print(min(timeit.Timer('_prefix_fun_slice(str_to_test)', setup).repeat(1, 10)))
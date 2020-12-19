def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    num_of_opened = 0
    num_of_closed = 0
    result = True
    for i in brackets_row:
        if i == '(':
            num_of_opened += 1
        else:
            num_of_closed += 1
        if num_of_closed > num_of_opened: result = False
    if result:
        if num_of_closed != num_of_opened:
            result = False
    return result

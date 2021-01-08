from typing import Union, Sequence

# Тут у меня не получилось (хотел по-другому написать) - не подскажите, где  я ощибся в логике?
def stairway_path_alternative(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    if len(stairway) == 1:
        return stairway[0]

    currStep = -1
    fullCost = 0
    while currStep < len(stairway) - 1:
        if currStep + 2 <= len(stairway) - 1:
            add_cost = min(stairway[currStep + 1], stairway[currStep + 2])
            add_step = 2 if stairway[currStep + 2] <= stairway[currStep + 1] else 1
            if add_step == 1:
                if len(stairway) - 1 - currStep > 0:
                    if stairway[currStep + 3] >= stairway[currStep + 2]:
                        add_step = 2
                        add_cost = stairway[currStep + 2]
            fullCost += add_cost
            currStep += add_step
        else:
            fullCost += stairway[currStep + 1]
            currStep += 1

    return fullCost


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    if len(stairway) == 0:
        return 0

    if len(stairway) == 1:
        return stairway[0]

    sums_list = [0] * len(stairway)
    sums_list[0] = stairway[0]
    sums_list[1] = stairway[1]

    for s in range(2, len(stairway)):
        sums_list[s] = stairway[s] + min(sums_list[s - 1], sums_list[s - 2])
    return sums_list[-1]

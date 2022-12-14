from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    minimal_cost = 0
    for i in range(2, len(stairway)):
        stairway[i] = min(stairway[i - 2] + stairway[i], stairway[i - 1] + stairway[i])
    print(stairway)
    return stairway[-1]




import random
from typing import Iterable, Optional


def binary_search(seq: Iterable[int], key: int) -> Optional[int]:
    """docstring
    """
    left = 0
    right = len(seq) - 1

    while left <= right:
        mid = (left + right) // 2

        if key == seq[mid]:
            return mid

        elif key > seq[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return None


if __name__ == "__main__":
    MAX = 10**6
    arr = list(range(MAX))
    n = random.randint(0, MAX)

    assert isinstance(binary_search(arr, n), int)
    assert binary_search(arr, MAX) is None

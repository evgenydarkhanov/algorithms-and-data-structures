import random
from typing import Iterable, Optional


def linear_search(seq: Iterable[int], key: int) -> Optional[int]:
    """docstring
    """
    for i in range(len(seq)):
        if seq[i] == key:
            return i
    return None


if __name__ == "__main__":
    MAX = 10**6
    arr = list(range(MAX))
    n = random.randint(0, MAX)

    assert isinstance(linear_search(arr, n), int)
    assert linear_search(arr, MAX) is None

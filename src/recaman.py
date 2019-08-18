"""Recamán's sequence generator"""
from typing import Generator


def recaman(steps: int) -> Generator[int, None, None]:
    """Generate Recamán's sequence

    :param steps: amount of iterations / length of iterator
    :returns: None
    """
    previous = [0]

    for step in range(1, steps + 1):
        last = previous[-1]
        new = last - step

        if new in previous or new < 0:
            new = last + step

        previous.append(new)

        yield previous[-1]

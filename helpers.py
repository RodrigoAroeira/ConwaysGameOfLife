import random

type Matrix[T] = list[list[T]]


def genRandomGrid(rows, cols) -> Matrix[bool]:
    """Generates a random matrix of boolean values"""
    states = (False, True)
    return [[random.choice(states) for _ in range(cols)] for _ in range(rows)]

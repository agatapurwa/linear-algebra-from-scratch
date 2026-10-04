"""
Matrix and Vector Operations from Scratch
2. Linear Combination, Span, and Basis vector
"""

def scalar_multiplication(v: list[float], scalar: float) -> list[float]:
    """
    scale a vector with a scalar constant.

    Args:
        v: [x, y] or [x, y, z]
        scalar: scaling multiplier c

    Returns:
        New scaled vector v * c
    """

    # PSEUDO-CODE / GUIDE:
    # 1. Use a list comprehension to multiply each element in v by scalar.
    result_scalar_multiplication = [element * scalar for element in v]

    # 2. Return the resulting list.
    return result_scalar_multiplication


def vector_add(v1: list[float], v2: list[float]) -> list[float]:
    """
    Adds two vectors element wise.

    Args:
        v1: first vector as a list of floats.
        v2: second vector as a list of floats.

    Returns:
        A new vector list containing component-wise sums.
    """

    # PSEUDO-CODE:
    # 1. Validate that len(v1) == len(v2). If mismatched, raise ValueError.
    if len(v1) != len(v2):
        raise ValueError(f"Dimension mismatch: len(v1) = {len(v1)} != len(v2) = {len(v2)}")

    # 2. Return a list where each element is v1[i] + v2[i].
    # Fix: Hapus koma setelah (x + y)
    result_vector_add = [x + y for x, y in zip(v1, v2)]
    return result_vector_add


def linear_combination(vectors: list[list[float]], scalars: list[float]) -> list[float]:
    """
    Computes a linear combination of N vectors:
    c1*v1 + c2*v2+...+cn*vn

    
    """
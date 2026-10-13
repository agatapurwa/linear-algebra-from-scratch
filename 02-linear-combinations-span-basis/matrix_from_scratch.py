"""
Matrix and Vector Operations from Scratch
2. Linear Combination, Span, and Basis vector
"""

def scalar_multiplication(v: list[float], scalar: float) -> list[float]:
    """Scales a vector with a scalar constant."""
    return [x * scalar for x in v]


def vector_add(v1: list[float], v2: list[float]) -> list[float]:
    """Adds two vectors element-wise."""
    if len(v1) != len(v2):
        raise ValueError(f"Dimension mismatch: {len(v1)} != {len(v2)}")
    
    return [x + y for x, y in zip(v1, v2)]


def linear_combination(vectors: list[list[float]], scalars: list[float]) -> list[float]:
    """Computes a linear combination of N vectors: c1*v1 + c2*v2 + ... + cn*vn"""
    if len(vectors) != len(scalars):
        raise ValueError(f"Vectors count ({len(vectors)}) must match scalars count ({len(scalars)})")
    
    if not vectors:
        return []
    
    dim = len(vectors[0])
    if not all(len(v) == dim for v in vectors):
         raise ValueError("All vectors must have the same dimension")

    result = [0.0] * dim
    for v, s in zip(vectors, scalars):
        scaled_v = scalar_multiplication(v, s)
        result = vector_add(result, scaled_v)

    return result


def check_linear_dependence(v1: list[float], v2: list[float]) -> bool:
    """Checks if two 2D vectors are linearly dependent (collinear)."""
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError(f"Both vectors must be 2D. Received len(v1)={len(v1)}, len(v2)={len(v2)}.")

    # 2D cross-product / determinant
    det = (v1[0] * v2[1]) - (v1[1] * v2[0])
    return abs(det) < 1e-9


def generate_span_sample(v1: list[float], v2: list[float], c_range: list[float]) -> list[list[float]]:
    """Generates span points representing the linear combination of v1 and v2 within c_range."""
    return [linear_combination([v1, v2], [c1, c2]) for c1 in c_range for c2 in c_range]

        
if __name__ == "__main__":
    v1 = [3.0, 1.0]
    v2 = [1.0, 2.0]
    c1, c2 = 2.0, -1.5

    print(f"Scalar Multiplication ({c1} * {v1}) :", scalar_multiplication(v1, c1))
    print(f"Vector Addition ({v1} + {v2}) :", vector_add(v1, v2))
    print(f"Linear Combination ({c1}*v1 + {c2}*v2) :", linear_combination([v1, v2], [c1, c2]))
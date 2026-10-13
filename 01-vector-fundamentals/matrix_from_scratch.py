"""
Matrix and Vector Operations from Scratch
1. Vector Fundamentals
"""
def vector_add(v1: list[float], v2: list[float]) -> list[float]:
    """Adds two vectors component-wise."""
    if len(v1) != len(v2):
        raise ValueError(f"Dimension mismatch: {len(v1)} != {len(v2)}")

    return [x + y for x, y in zip(v1, v2)]


def dot_product(v1: list[float], v2: list[float]) -> float:
    """Computes the dot product of two vectors."""
    if len(v1) != len(v2):
        raise ValueError(f"Dimension mismatch: {len(v1)} != {len(v2)}")

    return sum(x * y for x, y in zip(v1, v2))


def matrix_multiply(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """Multiplies matrix A (m x n) by matrix B (n x p)."""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError(f"Cannot multiply: A cols ({cols_A}) != B rows ({rows_B})")

    # Transpose B for cleaner dot-product row-by-column computation
    B_T = list(zip(*B))
    return [[dot_product(row_a, col_b) for col_b in B_T] for row_a in A]


if __name__ == "__main__":
    v1 = [1.0, 2.0, 3.0]
    v2 = [4.0, 5.0, 6.0]

    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]

    print("Vector Add:", vector_add(v1, v2))
    print("Dot Product:", dot_product(v1, v2))
    print("Matrix Multiply:", matrix_multiply(A, B))
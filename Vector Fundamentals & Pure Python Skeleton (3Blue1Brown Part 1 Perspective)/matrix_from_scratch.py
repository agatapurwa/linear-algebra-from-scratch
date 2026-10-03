def vector_add(v1: list[float], v2: list[float]) -> list[float]:
    """
    Adds two vectors component-wise (Tip-to-Tail geometric sum).
    
    Args:
        v1: First vector as a list of floats.
        v2: Second vector as a list of floats.

    Returns:
        A new vector list containing component-wise sums.    
    """
    # PSEUDO-CODE / GUIDE:
    # 1. Check if len(v1) == len(v2). If not, raise ValueError("Dimension mismatch").
    if len(v1) != len(v2):
        raise ValueError(f"Dimension mismatch: len(v1)={len(v1)} != len(v2)={len(v2)}")

    # 2. Create an empty list for the result: result = []
    result = []

    # 3. Loop through indices from 0 to len(v1) - 1 (or use zip(v1, v2)):
    #       - Calculate sum of corresponding elements: v1[i] + v2[i]
    #       - Append sum to result list
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
                      
    # 4. Return result
    return result # Replaces 'pass'

def dot_product(v1: list[float], v2: list[float]) -> float:
    """
    Computes the dot product (scalar product) of two equal-length vectors.

    Args:
        v1: First vector as a list of floats.
        v2: Second vector as a list of floats.

    Returns:
        The scalar result (sum of element-wise products).
    """
    # PSEUDO-CODE / GUIDE:
    # 1. Check if len(v1) == len(v2). If not, raise ValueError("Dimension mismatch").
    if len(v1) != len(v2):
        raise ValueError(f"Dimension mismatch: len(v1)={len(v1)} != len(v2)={len(v2)}")
    
    # 2. Initialize a float variable total_sum = 0.0
    total_sum = 0.0

    # 3. Loop through indices i (or zip(v1, v2)):
    #       - Multiply v1[i] * v2[i]
    #       - Add product to total_sum
    for i in range (len(v1)):
        total_sum += v1[i] * v2[i]

    # 4. Return total_sum
    return total_sum # Replaces pass

def matrix_multiply(A: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """
    Multiplies matrix A (m x n) by matrix B (n x p) from scratch.

    Args:
        A: 2D list representing an m x n matrix.
        B: 2D list representing an n x p matrix.

    Returns:
        A new 2D list representing the resulting m x p matrix.
    """
    # PSEUDO-CODE / GUIDE:
    # 1. Get dimensions:
    #    - rows_A = len(A)
    #    - cols_A = len(A[0])
    #    - rows_B = len(B)
    #    - cols_B = len(B[0])
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # 2. Validate condition for matrix multiplication:
    #    - Check if cols_A == rows_B. If not, raise ValueError("Cannot multiply matrices").
    if cols_A != rows_B:
        raise ValueError (f"Cannot multiply matrices columns of A ({cols_A}) must match rows of B ({rows_B})")

    # 3. Initialize result matrix C of size (rows_A x cols_B) filled with 0.0:
    #    - C = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    C = [[0.0 for _ in range (cols_B)] for _ in range (rows_A)]

    # 4. Implement Triple Nested Loop (or use dot_product on row A[i] and col B[:][j]):
    #    - Outer loop i from 0 to rows_A - 1 (Iterate rows of A)
    #      - Middle loop j from 0 to cols_B - 1 (Iterate columns of B)
    #        - Inner loop k from 0 to cols_A - 1:
    #          - C[i][j] += A[i][k] * B[k][j]
    for i in range (rows_A):
        for j in range (cols_B):
            for k in range (cols_A):
                C[i][j] += A[i][k] * B[k][j]

    # 5. Return result matrix C
    return C #Replaces pass

if __name__ == "__main__":
    # Test Vector Addition
    v1 = [1.0, 2.0, 3.0]
    v2 = [4.0, 5.0, 6.0]
    # Expected output: [5.0, 7.0, 9.0]

    # Test Dot Product
    # Expected output: (1*4) + (2*5) + (3*6) = 32.0
    print("Dot Product:", dot_product(v1, v2))

    # Test Matrix Multiplication
    A = [
        [1.0, 2.0],
        [3.0, 4.0]
    ]
    B = [
        [5.0, 6.0],
        [7.0, 8.0]
    ]
    # Expected output: [[19.0, 22.0], [43.0, 50.0]]
    print("Matrix Multiply:", matrix_multiply(A, B))

    
# =====================================================================
# MODULE: Matrix Multiplication as Composition from Scratch
# BASED ON: 3Blue1Brown Chapter 4 - Matrix Multiplication as Composition
# =====================================================================

def matrix_multiply(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    """
    Computes the product of two 2x2 matrices (C = A * B) by treating it
    as the composition of two linear transformations: applying matrix B 
    first, followed by matrix A.

    Args:
        matrix_a: Left 2x2 matrix [[a, b], [c, d]] (applied second)
        matrix_b: Right 2x2 matrix [[e, f], [g, h]] (applied first)

    Returns:
        Resultant 2x2 composite matrix as a list[list[float]]
    """
    # 1. Validate that both matrices are valid 2x2 dimensions
    if (len(matrix_a) != 2 or len(matrix_a[0]) != 2 or len(matrix_a[1]) != 2 or 
        len(matrix_b) != 2 or len(matrix_b[0]) != 2 or len(matrix_b[1]) != 2):
        raise ValueError('All matrices must be 2x2 valid matrices.')

    # 2. Extract Columns of Matrix B (Intermediate landing spots for i-hat and j-hat)
    t_i_hat = [matrix_b[0][0], matrix_b[1][0]]  # Column 1 of B
    t_j_hat = [matrix_b[0][1], matrix_b[1][1]]  # Column 2 of B

    # 3. Extract elements of Matrix A
    a, b = matrix_a[0][0], matrix_a[0][1]
    c, d = matrix_a[1][0], matrix_a[1][1]

    # 4. Transform Columns using Matrix A (Matrix-Vector Multiplication)
    # Final position of i-hat = Matrix A * Column 1 of B
    col1_final = [
        (a * t_i_hat[0]) + (b * t_i_hat[1]),
        (c * t_i_hat[0]) + (d * t_i_hat[1])
    ]

    # Final position of j-hat = Matrix A * Column 2 of B
    col2_final = [
        (a * t_j_hat[0]) + (b * t_j_hat[1]),
        (c * t_j_hat[0]) + (d * t_j_hat[1])
    ]

    # 5. Construct and return the 2x2 composite matrix in row-major format
    return [
        [col1_final[0], col2_final[0]],  # Row 0: [col1_x, col2_x]
        [col1_final[1], col2_final[1]]   # Row 1: [col1_y, col2_y]
    ]


if __name__ == "__main__":
    # Test Data from Chapter 4 Examples
    matrix_a = [[1.0, 2.0], [3.0, 4.0]]
    matrix_b = [[5.0, 6.0], [7.0, 8.0]]

    # Run Matrix Multiplication (Composition)
    result = matrix_multiply(matrix_a, matrix_b)
    print("=== MATRIX MULTIPLICATION COMPOSITION TEST ===")
    print(result)  # Expected Output: [[19.0, 22.0], [43.0, 50.0]]
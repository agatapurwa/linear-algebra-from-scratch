"""
Matrix Multiplication as Composition from Scratch
4. Matrix Multiplication as Composition
"""

def _validate_2d_matrix(matrix: list[list[float]]) -> None:
    """Helper function to validate 2x2 matrix dimensions."""
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("Matrix must be 2x2.")


def matrix_multiply(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    """
    Computes C = A * B by applying transformation B first, followed by transformation A.
    """
    _validate_2d_matrix(matrix_a)
    _validate_2d_matrix(matrix_b)

    # Columns of B (intermediate basis landings)
    b_col1 = [matrix_b[0][0], matrix_b[1][0]]
    b_col2 = [matrix_b[0][1], matrix_b[1][1]]

    # Transform columns of B using Matrix A
    a, b = matrix_a[0][0], matrix_a[0][1]
    c, d = matrix_a[1][0], matrix_a[1][1]

    col1 = [a * b_col1[0] + b * b_col1[1], c * b_col1[0] + d * b_col1[1]]
    col2 = [a * b_col2[0] + b * b_col2[1], c * b_col2[0] + d * b_col2[1]]

    return [
        [col1[0], col2[0]],
        [col1[1], col2[1]]
    ]


if __name__ == "__main__":
    matrix_a = [[1.0, 2.0], [3.0, 4.0]]
    matrix_b = [[5.0, 6.0], [7.0, 8.0]]

    result = matrix_multiply(matrix_a, matrix_b)
    print("Matrix Composition (A * B) :", result)
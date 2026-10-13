"""
Matrix and Vector Operations from Scratch
3. Linear Transformations & Matrix Transformations
"""

def _validate_2d_matrix(matrix: list[list[float]]) -> None:
    """Helper function to validate 2x2 matrix dimensions."""
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("Matrix must be 2x2.")


def matrix_vector_multiply(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Computes the transformation T(v) = M * v for 2D vectors."""
    _validate_2d_matrix(matrix)
    if len(vector) != 2:
        raise ValueError(f"Vector must be 2D. Received length {len(vector)}.")

    x, y = vector
    # Kolom 1 (t_i_hat) dan Kolom 2 (t_j_hat)
    return [
        matrix[0][0] * x + matrix[0][1] * y,
        matrix[1][0] * x + matrix[1][1] * y
    ]


def check_dimensionality_reduction(matrix: list[list[float]]) -> bool:
    """Checks if a 2D matrix collapses space into a 1D line (determinant ≈ 0)."""
    _validate_2d_matrix(matrix)

    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    det = a * d - b * c

    return abs(det) < 1e-9


def get_rotation_90_ccw_matrix() -> list[list[float]]:
    """Returns a 2x2 matrix for 90-degree counter-clockwise rotation."""
    return [
        [0.0, -1.0],
        [1.0,  0.0]
    ]


def get_shear_horizontal_matrix() -> list[list[float]]:
    """Returns a 2x2 matrix for a horizontal shear transformation."""
    return [
        [1.0, 1.0],
        [0.0, 1.0]
    ]


if __name__ == "__main__":
    v = [2.0, 3.0]

    rot_matrix = get_rotation_90_ccw_matrix()
    print("90° CCW Rotation :", matrix_vector_multiply(rot_matrix, v))

    shear_matrix = get_shear_horizontal_matrix()
    print("Horizontal Shear :", matrix_vector_multiply(shear_matrix, v))

    collapse_matrix = [[1.0, 2.0], [2.0, 4.0]]
    print("Is Collapsed?    :", check_dimensionality_reduction(collapse_matrix))

    not_collapse_matrix = [[2.0, 2.0], [2.0, 5.0]]
    print("Is Collapsed?    :", check_dimensionality_reduction(not_collapse_matrix))
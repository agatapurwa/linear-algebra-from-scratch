import math

"""
3D Matrix and Vector Operations from Scratch
5. Three-Dimensional Linear Transformations
"""


def vector_add_3d(v1: list[float], v2: list[float]) -> list[float]:
    """Adds two 3D vectors component-wise (x1 + x2, y1 + y2, z1 + z2)."""
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError(f"Both vectors must be 3-dimensional. Got lengths {len(v1)} and {len(v2)}.")

    return [x + y for x, y in zip(v1, v2)]


def scalar_multiply_3d(scalar: float, v: list[float]) -> list[float]:
    """Scales a 3D vector component-wise by a scalar constant (s * x, s * y, s * z)."""
    if len(v) != 3:
        raise ValueError(f"Expected a 3D vector, but got length {len(v)}.")

    return [scalar * x for x in v]


def _validate_3d_matrix(matrix: list[list[float]]) -> None:
    """Helper function to validate 3x3 matrix dimensions."""
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("Matrix must be a 3x3 grid.")


def matrix_vector_multiply_3d(matrix: list[list[float]], v: list[float]) -> list[float]:
    """Computes a linear combination of 3x3 matrix columns weighted by vector v components."""
    if len(v) != 3:
        raise ValueError(f"Vector must be 3-dimensional, got length {len(v)}.")

    _validate_3d_matrix(matrix)

    # 1. Extract matrix columns (Vertical basis vectors)
    col1 = [matrix[0][0], matrix[1][0], matrix[2][0]]
    col2 = [matrix[0][1], matrix[1][1], matrix[2][1]]
    col3 = [matrix[0][2], matrix[1][2], matrix[2][2]]

    # 2. Compute linear combination: x*col1 + y*col2 + z*col3
    x_col1 = scalar_multiply_3d(v[0], col1)
    y_col2 = scalar_multiply_3d(v[1], col2)
    z_col3 = scalar_multiply_3d(v[2], col3)

    # 3. Add the three vectors sequentially
    sum_xy = vector_add_3d(x_col1, y_col2)

    return vector_add_3d(sum_xy, z_col3)


def matrix_multiply_3d(m1: list[list[float]], m2: list[list[float]]) -> list[list[float]]:
    """
    Computes C = M1 * M2 by transforming each column vector of M2 using M1.
    Aligns with Module 04 composition logic.
    """
    _validate_3d_matrix(m1)
    _validate_3d_matrix(m2)

    # 1. Extract columns of M2 (the intermediate basis vectors)
    m2_col1 = [m2[0][0], m2[1][0], m2[2][0]]
    m2_col2 = [m2[0][1], m2[1][1], m2[2][1]]
    m2_col3 = [m2[0][2], m2[1][2], m2[2][2]]

    # 2. Transform each column of M2 through M1
    res_col1 = matrix_vector_multiply_3d(m1, m2_col1)
    res_col2 = matrix_vector_multiply_3d(m1, m2_col2)
    res_col3 = matrix_vector_multiply_3d(m1, m2_col3)

    # 3. Reconstruct into a 3x3 matrix (Row by Row)
    return [
        [res_col1[0], res_col2[0], res_col3[0]],
        [res_col1[1], res_col2[1], res_col3[1]],
        [res_col1[2], res_col2[2], res_col3[2]]
    ]


def get_rotation_matrix_y(angle_rad: float) -> list[list[float]]:
    """Returns a 3x3 Y-axis rotation matrix for a given angle in radians."""
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)

    return [
        [cos_theta,  0.0,  sin_theta],
        [0.0,        1.0,  0.0      ],
        [-sin_theta, 0.0,  cos_theta]
    ]


if __name__ == "__main__":
    # Test Vector Addition
    v1 = [1.0, 2.0, 3.0]
    v2 = [4.0, 5.0, 6.0]
    print("Vector Add 3D          :", vector_add_3d(v1, v2))

    # Test Y-Axis Rotation (90 degrees = pi/2 radians)
    rot_y_90 = get_rotation_matrix_y(math.pi / 2)
    
    # Rotate i-hat [1, 0, 0] around Y-axis -> should land near [0, 0, -1]
    i_hat = [1.0, 0.0, 0.0]
    transformed_i = matrix_vector_multiply_3d(rot_y_90, i_hat)
    print("Transformed i-hat (RotY):", [round(x, 2) for x in transformed_i])

    # Test Matrix Composition
    m1 = [[1.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 3.0]]
    m2 = [[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]]
    print("Matrix Composition 3D   :", matrix_multiply_3d(m1, m2))
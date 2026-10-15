def vector_add_3d(v1: list[float], v2: list[float]) -> list[float]:
    """ Adding two 3D vectors (x1 + x2, y1 + y2, z1 + z2)"""
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError (f'Both vectors must be 3-dimensional. Got lengths {len(v1)} != {len(v2)}')

    return [x + y for x, y in zip(v1, v2)]

def scalar_multiply_3d(scalar: float, v: list[float]) -> list[float]:
    """Scales a 3D vector component-wise by a scalar constant (s * x, s * y, s * z)."""
    if len(v) != 3:
        raise ValueError(f"Expected a 3D vector, but got length {len(v)}.")
    
    return [scalar * x for x in v]

def matrix_vector_multiply_3d(matrix: list[list[float]], v: list[float]) -> list[float]:
    """Computes a linear combination of 3x3 matrix columns weighted by vector v components."""
    #1. Validate vector dimension
    if len(v) != 3:
        raise ValueError (f'Vector must be 3-dimensional, got length {len(v)}.')

    #2. Validate matrix dimensions (must be 3x3)
    # Check row count first)
    if len(matrix) != 3:
        raise ValueError("Matrix must have 3 rows.")
    # Check column count for EVERY row
    if any(len(row) != 3 for row in matrix):
        raise ValueError("Every row in the matrix must have 3 columns.")

    #3. Extract matrix columns
    col1 = [matrix[0][0], matrix[1][0], matrix[2][0]]
    col2 = [matrix[0][1], matrix[1][1], matrix[2][1]]
    col3 = [matrix[0][2], matrix[1][2], matrix[2][2]]

    # 4. Compute x*col1 + y*col2 + z*col3
    x_col1 = scalar_multiply_3d(v[0], col1)
    y_col2 = scalar_multiply_3d(v[1], col2)
    z_col3 = scalar_multiply_3d(v[2], col3)
    
    # Add the three vectors step-by-step
    sum_xy = vector_add_3d(x_col1, y_col2)
    
    return vector_add_3d(sum_xy, z_col3)

def matrix_multiply_3d(m1: list[list[float]], m2: list[list[float]]) -> list[list[float]]:
    """"""

def get_rotation_matrix_y(angle_rad: float) -> list[list[float]]:
    """"""
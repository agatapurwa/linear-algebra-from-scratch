def matrix_vector_multiply(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """
    Computes the transformatin T(v) = M * v by evaluating the linear
    combination of transformed vectors.

    Args:
        matrix: 2x2 matrix represented as list of row lists [[a, b], [c, d]]
        vector: 2D vector represented as [x, y]

    Returns:
        Resultant transformed vector as a list[float]
    """

    #1. Check if the matrix rows and vector have the correct 2D dimension
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) !=2:
        raise ValueError ("Matrix must be 2x2.")
    if len(vector) != 2:
        raise ValueError(f"Vector must be 2D. Received length {len(vector)}.")
    
    #2. Extract basis vector landing coordinates (Columns)
    # Column 1: Where i-hat lands [a, c]
    t_i_hat = [matrix[0][0], matrix[1][0]]

    # Column 2: Where j-hat lands [b, d]
    t_j_hat = [matrix[0][1], matrix[1][1]]

    #3. Compute Linear Combination
    # Extract scalars x = vector[0] and y = vector[1].
    x, y = vector[0], vector[1]

    # x * t_i_hat + y * t_j_hat
    new_x = (vector[0] * t_i_hat[0] + vector[1] * t_j_hat[0])
    new_y = (vector[0] * t_i_hat[1] + vector[1] * t_j_hat[1])

    return [new_x, new_y]

def check_dimensionality_reduction(matrix: list[list[float]]) -> bool:
    """
    Checks if a 2D linear transformation collapses (squishes) 2D space
    down into a 1D line span by checking for collinear basis vectors.

    Args:
        matrix: 2x2 matrix [[a, b], [c, d]]
    
    Returns:
        True if space collapses to 1D (determinant ≈ 0), False otherwise.
    """
    #1. Check if the matrix rows and vector have the correct 2D dimension
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) !=2:
        raise ValueError ("Matrix must be 2x2.")

    #2. Determinant Calculation:
    # Extract matrix elements: [[a, b], [c, d]]
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    # Calculate the 2D determinant det(M) = ad - bc
    det_m = (a*d - b*c)

    #3. Floating-Point Comparison
    # Due to IEEE float precision limits, exact zero determinants can evaluate to ~1e-16.
    # Checking abs(det) < 1e-9 prevents false negatives when det is mathematically 0.0.
    return abs(det_m) < 1e-9

def get_rotation_90_ccw_matrix() -> list[list[float]]:
    """
    Rotates space 90 degrees counter-clockwise.
    - i-hat (1,0) lands at (0, 1)   -> Column 1
    - j-hat (0,1) lands at (-1, 0)  -> Column 2

    Returns the 2x2 matrix representing a 90-degree counter-clockwise rotation.
    """
    return [
        [ 0.0, -1.0],
        [ 1.0,  0.0]
    ]

def get_shear_horizontal_matrix() -> list[list[float]]:
    """
    Performs a horizontal shear.
    - i-hat (1,0) remains fixed at (1, 0) -> Column 1
    - j-hat (0,1) shifts to (1, 1)        -> Column 2

    Returns the 2x2 matrix reprensting a horizontal shear. 
    """
    return [
        [1.0, 1.0],
        [0.0, 1.0]
    ]
if __name__ == "__main__":
    v = [2.0, 3.0]

# Test 1: 90-degree CCW Rotation on vector [2.0, 3.0]
    # Expected result: [-3.0, 2.0]
    rot_matrix = get_rotation_90_ccw_matrix()
    rotated_v = matrix_vector_multiply(rot_matrix, v)
    print("Test 1 (90° CCW Rotation) :", rotated_v)

    # Test 2: Horizontal Shear on vector [2.0, 3.0]
    # Expected result: [5.0, 3.0]
    shear_matrix = get_shear_horizontal_matrix()
    shear_v = matrix_vector_multiply(shear_matrix, v)
    print("Test 2 (horizontal shear) :", shear_v)

    # Test 3: Dimensionality Collapse Matrix (e.g., [[1.0, 2.0], [2.0, 4.0]])
    # Expected check_dimensionality_reduction: True
    collapse_matrix = [[1.0, 2.0], [2.0, 4.0]]
    is_collapsed = check_dimensionality_reduction(collapse_matrix)
    print("Test 3 (Is Collapsed?)    :", is_collapsed)

    # Test 4: Dimensionality Collapse Matrix (e.g., [[2.0, 2.0], [2.0, 5.0]])
    # Expected check_dimensionality_reduction: False
    not_collapse_matrix = [[2.0, 2.0], [2.0, 5.0]]
    is_not_collapsed = check_dimensionality_reduction(not_collapse_matrix)
    print("Test 4 (Is Collapsed?)    :", is_not_collapsed)
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

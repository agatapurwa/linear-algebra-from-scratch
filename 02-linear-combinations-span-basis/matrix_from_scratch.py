"""
Matrix and Vector Operations from Scratch
2. Linear Combination, Span, and Basis vector
"""

def scalar_multiplication(v: list[float], scalar: float) -> list[float]:
    """
    scale a vector with a scalar constant.

    Args:
        v: [x, y] or [x, y, z]
        scalar: scaling multiplier c

    Returns:
        New scaled vector v * c
    """

    # PSEUDO-CODE / GUIDE:
    # 1. Use a list comprehension to multiply each element in v by scalar.
    result_scalar_multiplication = [element * scalar for element in v]

    # 2. Return the resulting list.
    return result_scalar_multiplication


def vector_add(v1: list[float], v2: list[float]) -> list[float]:
    """
    Adds two vectors element wise.

    Args:
        v1: first vector as a list of floats.
        v2: second vector as a list of floats.

    Returns:
        A new vector list containing component-wise sums.
    """

    # PSEUDO-CODE:
    # 1. Validate that len(v1) == len(v2). If mismatched, raise ValueError.
    if len(v1) != len(v2):
        raise ValueError(f"Dimension mismatch: len(v1) = {len(v1)} != len(v2) = {len(v2)}")

    # 2. Return a list where each element is v1[i] + v2[i].
    result_vector_add = [x + y for x, y in zip(v1, v2)]
    return result_vector_add


def linear_combination(vectors: list[list[float]], scalars: list[float]) -> list[float]:
    """
    Computes a linear combination of N vectors:
    c1*v1 + c2*v2+...+cn*vn

    Args:
        vectors: list of vectors, e.g., [[1.0, 0.0], [0.0, -1.0]]  
        scalars: list of scalar multiplier, e.g., [1.0, 2.0]

    Returns:
        Returns: resultant vector as a list[float]
    """
    
    # PSEUDO-CODE / GUIDE:
    #1. Check that len(vectors) == len(scalars). If not, raise ValueError.
    if len(vectors) != len(scalars):
        raise ValueError (f"The number of vectors {len(vectors)} must match the number of scalars {len(scalars)}")
    
    if not vectors:
        return []
    
    #2. Check that all vectors have the same dimension (length)
    dim = len(vectors[0])
    if not all(len(v) == dim for v in vectors):
         raise ValueError("All vectors must have the same dimension")

    #3. Initialize a resultant vector of zeros with length equal to vector dimension
    resultant = [0.0] * dim

    #4. Loop through each vector and its corresponding scalar:
    #   - Scale the vector using scalar_multiplication()
    #   - Add the scaled vector to resultant using vector_add()
    for v, s in zip(vectors, scalars):
        scaled_v = scalar_multiplication(v, s)
        resultant = vector_add(resultant, scaled_v)

    #5. Return the final resultant vector
    return resultant

def check_linear_depedance(v1: list[float], v2: list[float]) -> list[float]:
    """
    Checks if two 2D vectors are literally dependant (collinear)

    Args: 
        v1: 2D vector [x1, y1]
        v2: 2D vector [x2, y2]

    Returns:
        True if vector are linearly dependant, False if linearly independant
    """

    #PSEUDO-CODE GUIDE:
    #1. Ensure both vectors are 2D (len == 2)
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError (f"Both vectors must be 2D. Received len(v1)={len(v1)}, len(v2)={len(v2)}.")

    #2. Compute the 2D cross-product / determinant: 
    det = (v1[0] * v2[1]) - (v1[1] * v2[0])

    # 3. If determinant is zero (or within a tiny floating-point epsilon like 1e-9),
    #    the vectors are collinear (linearly dependent). Return True.
    # 4. Otherwise, return False.
    return abs(det) < 1e-9

if __name__ == "__main__":
    # Test Data
    v1 = [3.0, 1.0]
    v2 = [1.0, 2.0]
    c1, c2 = 2.0, -1.5

    # Run Operations
    scaled = scalar_multiplication(v1, c1)
    added = vector_add(v1, v2)
    combo = linear_combination([v1, v2], [c1, c2])

    # Print Proofs to Terminal
    print("=== MATRIX & VECTOR OPERATIONS TEST ===")
    print(f"Scalar Multiplication ({c1} * {v1}) : {scaled}")
    print(f"Vector Addition ({v1} + {v2})        : {added}")
    print(f"Linear Combination ({c1}*v1 + {c2}*v2) : {combo}")

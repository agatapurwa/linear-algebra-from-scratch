class Matrix:
    """Class representing general m x n matrices and cross-dimensional linear transformations."""

    def __init__(self, data: list[list[float]]) -> None:
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0
        self._validate()

    def _validate(self) -> None:
        """Ensures all rows have consistent lengths and matrix is non-empty."""
        if self.rows == 0 or self.cols == 0:
            raise ValueError("Matrix cannot be empty.")
        if any(len(row) != self.cols for row in self.data):
            raise ValueError("Invalid matrix layout: All rows must have equal length.")

    @property
    def shape(self) -> tuple[int, int]:
        """Returns matrix dimensions as (rows, cols) -> (m, n)."""
        return (self.rows, self.cols)

    @property
    def input_dim(self) -> int:
        """Returns dimension of input space (number of columns n)."""
        return (self.cols)

    @property
    def output_dim(self) -> int:
        """Returns dimension of output space (number of rows m)."""
        return (self.rows)

    def multiply_vector(self, v: list[list[float]]) -> list[float]:
        """Transforms vector v from R^n to R^m via linear combination of columns."""
        if len(v) != self.input_dim:
            raise ValueError(f"Vector dimension ({len(v)}) must match input_dim ({self.input_dim}).")

        # Compute L(v) = sum(v[j] * column_j) for j in range(n)
        return [
            sum(v[j] * self.data[i][j] for j in range(self.cols)) 
            for i in range(self.rows)
        ]

    def multiply_matrix(self, other: "Matrix") -> "Matrix":
        """Composes two transformations: (m x n) * (n x p) -> (m x p)."""
        if self.cols != other.rows:
            raise ValueError(f"Cannot multiply {self.shape} with {other.shape}: Inner dimensions mismatch.")

        # Compute the dot product for every row of 'self' and every column of 'other'
        result_data = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]

        return Matrix(result_data)

    def __repr__(self):
        """String representation showing shape and data."""
        return f"Matrix({self.rows}x{self.cols}, data={self.data})"


if __name__ == "__main__":
    # Test 1: 3x2 Matrix (2D Input -> 3D Output)
    M_3x2 = Matrix([[2.0, 0.0], [-1.0, 1.0], [-2.0, 1.0]])
    v_2d = [1.0, 2.0]
    out_3d = M_3x2.multiply_vector(v_2d)

    print("=== Test 1: 2D to 3D Transformation (3x2) ===")
    print(f"Matrix shape : {M_3x2.shape} (Input: R^{M_3x2.input_dim} -> Output: R^{M_3x2.output_dim})")
    print(f"Input vector : {v_2d}")
    print(f"Output vector: {out_3d}")
    print()

    # Test 2: 1x2 Matrix (2D Input -> 1D Scalar Line)
    M_1x2 = Matrix([[2.0, 7.0]])
    out_1d = M_1x2.multiply_vector(v_2d)

    print("=== Test 2: 2D to 1D Transformation (1x2) ===")
    print(f"Matrix shape : {M_1x2.shape}")
    print(f"Input vector : {v_2d}")
    print(f"Output scalar: {out_1d}")
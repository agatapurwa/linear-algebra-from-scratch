class Matrix:
    """Class for representing and operating on 2D & 3D Matrices (Extended for Module 07).""" 

    def __init__(self, data: list[list[float]]) -> None:
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0
        self._validate()

    def _validate(self) -> None:
        """Internal helper to ensure the matrix is a valid 2x2 or 3x3 square grid."""
        # Ensure that each row has a consistent number of elements
        if any(len(row) != self.cols for row in self.data):
            raise ValueError("Invalid matrix layout: All rows must have equal length.")

        # Check whether the matrix size is exactly 2x2 or 3x3.
        is_2x2 = (self.rows == 2 and self.cols == 2)
        is_3x3 = (self.rows == 3 and self.cols == 3)

        if not (is_2x2 or is_3x3):
            raise ValueError("Matrix must be a square grid of size 2x2 or 3x3.")

    def _det_2d(self) -> float:
        """Calculating the determinant of a 2x2 matrix (ad - bc)."""
        a, b = self.data[0][0], self.data[0][1]
        c, d = self.data[1][0], self.data[1][1]

        return a * d - b * c

    def _det_3d(self) -> float:
        """Calculating the determinant of a 3x3 matrix using first row cofactor expansion."""
        # Row 1
        a, b, c = self.data[0][0], self.data[0][1], self.data[0][2]
        # Row 2
        d, e, f = self.data[1][0], self.data[1][1], self.data[1][2]
        # Row 3
        g, h, i = self.data[2][0], self.data[2][1], self.data[2][2]

        return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    @property
    def det(self) -> float:
        """Dynamic attribute for obtaining the determinant value."""
        if self.rows == 2:
            return self._det_2d()
        elif self.rows == 3:
            return self._det_3d()
        raise ValueError("Determinants are only supported for 2x2 and 3x3 matrices.")

    @property
    def is_singular(self) -> bool:
        """Checking whether the matrix has undergone dimensional collapse (det = 0)."""
        return abs(self.det) < 1e-9

    @property
    def orientation_status(self) -> str:
        """Checking whether the spatial orientation is preserved, inverted, or collapsed."""
        if self.is_singular:
            return "Collapsed (Zero Area)"
        elif self.det > 0:
            return "Orientation Preserved"
        return "Orientation Inverted (Space Flipped)"

    def inverse(self) -> "Matrix":
        """Calculates and returns the inverse matrix (A^-1). Raises ValueError if singular."""
        if self.is_singular:
            raise ValueError ("Matrix is singular (det = 0) and cannot be inverted.")

        if self.rows == 2:
            det_val = self.det
            a, b = self.data[0][0], self.data[0][1]
            c, d = self.data[1][0], self.data[1][1]

            # Adjugate formula divided by determinant: (1/det) * [[d, -b], [-c, a]]
            inv_data = [
                [d / det_val, -b / det_val],
                [-c / det_val, a / det_val],
            ]
            return Matrix(inv_data)
        raise NotImplementedError("Inversion is currently only implemented for 2x2 matrices.")

    def solve(self, v: list[float]) -> list[float]:
        """Solves the linear system A*x = v for x by applying x = A^-1 * v."""
        if len(v) != self.cols:
            raise ValueError(f"Vector dimension ({len(v)}) must match matrix columns ({self.cols}).")

        inv_matrix = self.inverse()

        # Matrix-vector multiplication: x = A^-1 * v
        x = [
            sum(inv_matrix.data[i][j] * v[j] for j in range(inv_matrix.cols))
            for i in range(inv_matrix.rows)
        ]
        return x

    @property
    def rank(self) -> int:
        """Returns the dimension of the column space (Rank)."""
        if self.is_singular:
            return self.rows

        # Check if all elements are zero (Rank 0)
        all_zero = all(abs(val) < 1e-9 for row in self.data for val in row)
        if all_zero:
            return 0

        # For a 2x2 singular non-zero matrix, rank is always 1
        return 1
    
    @property
    def null_space_basis(self) -> list[list[float]]:
        """Finds the basis vector(s) spanning the null space (kernel)."""
        # Full rank: Only the zero vector lands at origin
        if not self.is_singular:
            return [[0.0] * self.cols]

        # Rank 0 (Zero matrix): All standard basis vectors are in the null space
        if self.rank == 0:
            return [[1.0 if i == j else 0.0 for j in range(self.cols)] for i in range(self.cols)]

        # Rank 1 (2x2): Extract non-trivial kernel direction [-b, a] or [-d, c]
        if self.rows == 2:
            a, b = self.data[0][0], self.data[0][1]
            c, d = self.data[1][0], self.data[1][1]

            vec = [-b, a] if (abs(a) > 1e-9 or abs(b) > 1e-9) else [-d, c]

            # Normalize the basis vector to unit length
            norm = (vec[0] ** 2 + vec[1] ** 2) ** 5
            if norm > 1e-9:
                vec = [round(vec[0] / norm, 4), round(vec[1]/ norm, 4)]

            return [vec]

        return[]

    def __repr__(self) -> str:
        """Displaying matrices visually in a neat format when printed."""
        return f"Matrix({self.data})"

if __name__ == "__main__":
    # 1. Full Rank Invertible Matrix Test
    A = Matrix([[2.0, 1.0], [1.0, 3.0]])
    v = [5.0, 10.0]

    A_inv = A.inverse()
    x = A.solve(v)

    print("=== Test 1: Full Rank System (A * x = v) ===")
    print(f"Matrix A          : {A}")
    print(f"Determinant det(A): {A.det}")
    print(f"Rank              : {A.rank}")
    print(f"Inverse A^-1      : {A_inv}")
    print(f"Target Vector v   : {v}")
    print(f"Solution Vector x : {x}")
    print(f"Null Space Basis  : {A.null_space_basis}")
    print()

    # 2. Singular Matrix Test (Rank Collapse)
    A_singular = Matrix([[2.0, -2.0], [1.0, -1.0]])

    print("=== Test 2: Singular Matrix (Rank 1 Collapse) ===")
    print(f"Matrix A          : {A_singular}")
    print(f"Determinant det(A): {A_singular.det}")
    print(f"Is Singular?      : {A_singular.is_singular}")
    print(f"Rank              : {A_singular.rank}")
    print(f"Null Space Basis  : {A_singular.null_space_basis}")
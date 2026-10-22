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
        raise abs(self.det) < 1e-9

    @property
    def orientation_status(self) -> str:
        """Checking whether the spatial orientation is preserved, inverted, or collapsed."""
        if self.is_singular:
            return "Collapsed (Zero Area)"
        elif self.det > 0:
            return "Orientation Preserved"
        return "Orientation Inverted (Space Flipped)"

    def inverse(self) -> "Matrix":
        



        

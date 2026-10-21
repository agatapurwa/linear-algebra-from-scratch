import os
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Import Matrix class from local matrix_from_scratch script
from matrix_from_scratch import Matrix


def transform_vector(matrix: Matrix, v: list[float]) -> list[float]:
    """Multiplies a 2x2 Matrix instance by a 2D vector [x, y]."""
    a, b = matrix.data[0][0], matrix.data[0][1]
    c, d = matrix.data[1][0], matrix.data[1][1]
    x, y = v[0], v[1]
    return [a * x + b * y, c * x + d * y]


def plot_determinant_area_scaling(matrix: Matrix) -> None:
    """
    Visualizes how a unit square scales its area based on the matrix determinant
    in 3Blue1Brown style, and exports the generated plot to assets/.
    """
    fig, ax = plt.subplots(figsize=(9, 8))

    # Dark background aesthetics (3Blue1Brown style)
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # Define original 2D unit square vertices: (0,0), (1,0), (1,1), (0,1)
    original_vertices = [
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
    ]

    # Transform vertices using the Matrix instance
    transformed_vertices = [
        transform_vector(matrix, v) for v in original_vertices
    ]

    # Transformed basis vectors
    i_hat_trans = transform_vector(matrix, [1.0, 0.0])
    j_hat_trans = transform_vector(matrix, [0.0, 1.0])

    # Grid lines & axes
    ax.axhline(0, color="gray", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.axvline(0, color="gray", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.grid(True, color="#333333", linestyle="--", alpha=0.5)

    # Original unit square (faint dotted gray outline)
    orig_polygon = Polygon(
        original_vertices,
        closed=True,
        fill=False,
        edgecolor="gray",
        linestyle=":",
        linewidth=1.5,
        label="Original Unit Square (Area = 1.0)",
    )
    ax.add_patch(orig_polygon)

    # Transformed polygon (yellow fill with transparency)
    trans_polygon = Polygon(
        transformed_vertices,
        closed=True,
        facecolor="yellow",
        alpha=0.35,
        edgecolor="yellow",
        linewidth=2,
        label=f"Transformed Area = {abs(matrix.det):.2f}",
    )
    ax.add_patch(trans_polygon)

    # Transformed basis vectors (quiver arrows)
    ax.quiver(
        0, 0,
        i_hat_trans[0], i_hat_trans[1],
        angles="xy", scale_units="xy", scale=1,
        color="#FF4136", linewidth=2.5, label="Transformed i-hat"
    )
    ax.quiver(
        0, 0,
        j_hat_trans[0], j_hat_trans[1],
        angles="xy", scale_units="xy", scale=1,
        color="#2ECC40", linewidth=2.5, label="Transformed j-hat"
    )

    # Dynamic view limits based on transformed polygon bounds
    all_x = [v[0] for v in transformed_vertices] + [0, 1]
    all_y = [v[1] for v in transformed_vertices] + [0, 1]
    margin = 1.5
    ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
    ax.set_ylim(min(all_y) - margin, max(all_y) + margin)

    # Ax aesthetics & spines
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("white")

    # Info overlay box
    info_text = (
        f"Matrix A:\n"
        f"  [{matrix.data[0][0]:.1f},  {matrix.data[0][1]:.1f}]\n"
        f"  [{matrix.data[1][0]:.1f},  {matrix.data[1][1]:.1f}]\n\n"
        f"det(A) = {matrix.det:.2f}\n"
        f"Area Factor = |det(A)| = {abs(matrix.det):.2f}\n"
        f"Status: {matrix.orientation_status}"
    )
    ax.text(
        0.03, 0.97, info_text,
        transform=ax.transAxes,
        color="white",
        fontsize=10,
        family="monospace",
        verticalalignment="top",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#111111", edgecolor="yellow", alpha=0.85),
    )

    plt.title(
        f"Determinant & Area Scaling Factor (det = {matrix.det:.2f})",
        color="white",
        pad=15,
        fontsize=13,
    )
    plt.legend(facecolor="#111111", labelcolor="white", loc="lower right")
    plt.tight_layout()

    # Save generated plot to assets/ directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    output_path = os.path.join(assets_dir, "determinant_scaling.png")
    plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor="none", bbox_inches="tight")

    plt.show()


if __name__ == "__main__":
    # Test matrix: Scale x by 3.0, Shear x by 1.0, Scale y by 2.0 -> det = 6.0
    matrix_a = Matrix([[3.0, 1.0], [0.0, 2.0]])
    plot_determinant_area_scaling(matrix_a)
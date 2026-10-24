import os
import matplotlib.pyplot as plt

# Import Matrix class from local module
from matrix_from_scratch import Matrix


def transform_vector(matrix_data: list[list[float]], v: list[float]) -> list[float]:
    """Multiplies a 2x2 matrix by a 2D vector [x, y]."""
    a, b = matrix_data[0][0], matrix_data[0][1]
    c, d = matrix_data[1][0], matrix_data[1][1]
    return [a * v[0] + b * v[1], c * v[0] + d * v[1]]


def draw_grid_lines(ax, matrix_data: list[list[float]], grid_range=12, color="#224466", alpha=0.35):
    """Draws dynamic transformed grid lines spanning across the viewable area."""
    for i in range(-grid_range, grid_range + 1):
        # Vertical grid line
        start_v = transform_vector(matrix_data, [i, -grid_range])
        end_v = transform_vector(matrix_data, [i, grid_range])
        ax.plot([start_v[0], end_v[0]], [start_v[1], end_v[1]], color=color, linestyle="--", alpha=alpha)

        # Horizontal grid line
        start_h = transform_vector(matrix_data, [-grid_range, i])
        end_h = transform_vector(matrix_data, [grid_range, i])
        ax.plot([start_h[0], end_h[0]], [start_h[1], end_h[1]], color=color, linestyle="--", alpha=alpha)


def plot_inverse_system_solving(A: Matrix, v: list[float]) -> None:
    """Visualizes Ax = v and x = A^-1 * v with clean, non-overlapping layouts."""
    if A.is_singular:
        raise ValueError("Cannot plot inverse system for a singular matrix (det = 0).")

    x = A.solve(v)
    A_inv = A.inverse()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5))
    fig.patch.set_facecolor("#0a0a0a")

    for ax in (ax1, ax2):
        ax.set_facecolor("#0a0a0a")
        ax.axhline(0, color="gray", linestyle="--", linewidth=0.8, alpha=0.5)
        ax.axvline(0, color="gray", linestyle="--", linewidth=0.8, alpha=0.5)
        ax.tick_params(colors="white")
        for spine in ax.spines.values():
            spine.set_color("#444444")

    # --- PANEL 1: Forward Space ---
    draw_grid_lines(ax1, A.data, grid_range=10, color="#1e3a5f")
    ax1.quiver(0, 0, x[0], x[1], angles="xy", scale_units="xy", scale=1,
               color="#FF79C6", linewidth=2.5, zorder=5, label=f"Input x = [{x[0]:.1f}, {x[1]:.1f}]")
    ax1.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1,
               color="#F1FA8C", linewidth=2.5, zorder=5, label=f"Target v = [{v[0]:.1f}, {v[1]:.1f}]")
    ax1.set_title("Forward Transformation: A · x = v", color="white", fontsize=11, pad=10)
    ax1.legend(facecolor="#111111", labelcolor="white", loc="upper left", framealpha=0.8)

    # --- PANEL 2: Inverse Space ---
    draw_grid_lines(ax2, A_inv.data, grid_range=15, color="#2ECC40", alpha=0.25)
    ax2.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1,
               color="#F1FA8C", linewidth=2.5, zorder=5, label=f"Target v = [{v[0]:.1f}, {v[1]:.1f}]")
    ax2.quiver(0, 0, x[0], x[1], angles="xy", scale_units="xy", scale=1,
               color="#FF79C6", linewidth=2.5, zorder=5, label=f"Recovered x = A⁻¹·v")
    ax2.set_title("Inverse Transformation: x = A⁻¹ · v", color="white", fontsize=11, pad=10)
    ax2.legend(facecolor="#111111", labelcolor="white", loc="upper left", framealpha=0.8)

    # Standardize Viewport Bounds
    for ax in (ax1, ax2):
        ax.set_xlim(-8, 12)
        ax.set_ylim(-8, 12)
        ax.set_aspect("equal")

    # Header Title Banner
    plt.suptitle("Linear System Solving via Inverse Matrix Transformation", color="white", fontsize=13, y=0.98)

    # Non-overlapping Subtitle Matrix Info
    info_header = (
        f"A = [[{A.data[0][0]:.1f}, {A.data[0][1]:.1f}], [{A.data[1][0]:.1f}, {A.data[1][1]:.1f}]]   |   "
        f"A⁻¹ = [[{A_inv.data[0][0]:.2f}, {A_inv.data[0][1]:.2f}], [{A_inv.data[1][0]:.2f}, {A_inv.data[1][1]:.2f}]]   |   "
        f"det(A) = {A.det:.2f}   |   Rank = {A.rank}"
    )
    fig.text(0.5, 0.92, info_header, color="#BD93F9", fontsize=9.5, family="monospace", ha="center")

    plt.tight_layout(rect=[0, 0, 1, 0.90])

    # Auto-export asset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    output_path = os.path.join(assets_dir, "linear_system_inverse.png")
    plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor="none")

    plt.show()


if __name__ == "__main__":
    A_matrix = Matrix([[2.0, 1.0], [1.0, 3.0]])
    v_target = [5.0, 10.0]
    plot_inverse_system_solving(A_matrix, v_target)
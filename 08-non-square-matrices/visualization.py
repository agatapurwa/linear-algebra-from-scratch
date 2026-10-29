import os
import matplotlib.pyplot as plt
from matrix_from_scratch import Matrix


def plot_nonsquare_transformation(M: Matrix) -> None:
    """
    Visualizes a 3x2 non-square transformation mapping 2D input space 
    to a 2D plane embedded inside 3D output space.
    """
    if M.shape != (3, 2):
        raise ValueError("This visualizer specifically expects a 3x2 matrix.")

    fig = plt.figure(figsize=(14, 6.5))
    fig.patch.set_facecolor("#0a0a0a")

    # Left Panel: 2D Input Space
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_facecolor("#0a0a0a")
    ax1.set_title("Input Space: ℝ² (2D Grid)", color="white", fontsize=11, pad=10)
    ax1.axhline(0, color="gray", linestyle="--", alpha=0.5)
    ax1.axvline(0, color="gray", linestyle="--", alpha=0.5)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.set_aspect("equal")
    ax1.tick_params(colors="white")

    # Input basis vectors
    ax1.quiver(0, 0, 1, 0, angles="xy", scale_units="xy", scale=1, color="#2ECC40", label="i-hat [1, 0]")
    ax1.quiver(0, 0, 0, 1, angles="xy", scale_units="xy", scale=1, color="#FF4136", label="j-hat [0, 1]")
    ax1.legend(facecolor="#111111", labelcolor="white", loc="upper left")

    # Right Panel: 3D Output Space
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    ax2.set_facecolor("#0a0a0a")
    ax2.set_title("Output Space: ℝ³ (Embedded 2D Plane)", color="white", fontsize=11, pad=10)

    # Extract transformed basis vectors (columns of matrix)
    i_land = [M.data[0][0], M.data[1][0], M.data[2][0]]
    j_land = [M.data[0][1], M.data[1][1], M.data[2][1]]

    # Plot transformed basis vectors in 3D
    ax2.quiver(0, 0, 0, i_land[0], i_land[1], i_land[2], color="#2ECC40", linewidth=2.5, label="L(i-hat)")
    ax2.quiver(0, 0, 0, j_land[0], j_land[1], j_land[2], color="#FF4136", linewidth=2.5, label="L(j-hat)")

    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_zlim(-3, 3)
    ax2.tick_params(colors="white")

    # Styling header text
    plt.suptitle(
        f"Non-Square Matrix Transformation: {M.rows}x{M.cols} (ℝ^{M.input_dim} → ℝ^{M.output_dim})",
        color="white", fontsize=13, y=0.98
    )

    # Auto-export asset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    output_path = os.path.join(assets_dir, "nonsquare_transformation.png")
    plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor="none")
    print(f"[+] Saved visualization asset to: {output_path}")

    plt.show()


if __name__ == "__main__":
    # Matrix mapping 2D -> 3D
    M_3x2 = Matrix([[2.0, 0.0], [-1.0, 1.0], [-2.0, 1.0]])
    plot_nonsquare_transformation(M_3x2)
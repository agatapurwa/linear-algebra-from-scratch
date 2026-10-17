import math
import matplotlib.pyplot as plt

# Import math fanctions form local script
from matrix_from_scratch import (
    get_rotation_matrix_y,
    matrix_vector_multiply_3d
)

def plot_3d_linear_transformation():
    """
    Visualizes 3D basis vector transformation using 
    Matplotlib mplot3d (3Blue1Brown Style).
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(projection="3d")

    # Dark background aesthetics
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # Define original 3D standard basis vectors
    i_hat = [1.0, 0.0, 0.0]  # Red (X-axis)
    j_hat = [0.0, 1.0, 0.0]  # Green (Y-axis)
    k_hat = [0.0, 0.0, 1.0]  # Cyan/Blue (Z-axis)

    # Apply 90-degree Y-axis rotation transformation
    transformation_matrix = get_rotation_matrix_y(math.pi / 2)

    i_hat_trans = matrix_vector_multiply_3d(transformation_matrix, i_hat)
    j_hat_trans = matrix_vector_multiply_3d(transformation_matrix, j_hat)
    k_hat_trans = matrix_vector_multiply_3d(transformation_matrix, k_hat)

    # Plot original axes (faint lines)
    ax.plot([-2, 2], [0, 0], [0, 0], color="gray", linestyle="--", alpha=0.5)
    ax.plot([0, 0], [-2, 2], [0, 0], color="gray", linestyle="--", alpha=0.5)
    ax.plot([0, 0], [0, 0], [-2, 2], color="gray", linestyle="--", alpha=0.5)

    # Plot original basis vectors (faint/dashed)
    ax.quiver(
        0,
        0,
        0,
        i_hat[0],
        i_hat[1],
        i_hat[2],
        color="red",
        alpha=0.3,
        linestyle=":",
    )
    ax.quiver(
        0,
        0,
        0,
        j_hat[0],
        j_hat[1],
        j_hat[2],
        color="green",
        alpha=0.3,
        linestyle=":",
    )
    ax.quiver(
        0,
        0,
        0,
        k_hat[0],
        k_hat[1],
        k_hat[2],
        color="cyan",
        alpha=0.3,
        linestyle=":",
    )

    # Plot transformed basis vectors (solid bold)
    ax.quiver(
        0,
        0,
        0,
        i_hat_trans[0],
        i_hat_trans[1],
        i_hat_trans[2],
        color="red",
        linewidth=2.5,
        label="Transformed i-hat",
    )
    ax.quiver(
        0,
        0,
        0,
        j_hat_trans[0],
        j_hat_trans[1],
        j_hat_trans[2],
        color="green",
        linewidth=2.5,
        label="Transformed j-hat",
    )
    ax.quiver(
        0,
        0,
        0,
        k_hat_trans[0],
        k_hat_trans[1],
        k_hat_trans[2],
        color="cyan",
        linewidth=2.5,
        label="Transformed k-hat",
    )

    # View limits and labels
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])

    ax.set_xlabel("X Axis", color="white")
    ax.set_ylabel("Y Axis", color="white")
    ax.set_zlabel("Z Axis", color="white")

    ax.tick_params(colors="white")
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor("black")
    ax.yaxis.pane.set_edgecolor("black")

    plt.title(
        "3D Linear Transformation (90° Rotation around Y-Axis)",
        color="white",
        pad=20,
    )
    plt.legend(facecolor="black", labelcolor="white")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_3d_linear_transformation()
import os
import matplotlib.pyplot as plt
from matrix_from_scratch import vector_add


def plot_vector_add(v1: list[float], v2: list[float]) -> None:
    """Plots two 2D vectors and their tip-to-tail sum on a Cartesian grid."""
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError("Only 2D vectors are supported for this plot.")

    v_sum = vector_add(v1, v2)

    fig, ax = plt.subplots(figsize=(8, 8))

    # 1. Vector 1 (Starts at origin)
    ax.quiver(
        0, 0, v1[0], v1[1],
        angles="xy", scale_units="xy", scale=1,
        color="#1f77b4", label=f"v1 = {v1}"
    )

    # 2. Vector 2 (Starts at the tip of v1)
    ax.quiver(
        v1[0], v1[1], v2[0], v2[1],
        angles="xy", scale_units="xy", scale=1,
        color="#ff7f0e", label=f"v2 = {v2} (Tip-to-Tail)"
    )

    # 3. Resultant Vector (Starts at origin to final tip)
    ax.quiver(
        0, 0, v_sum[0], v_sum[1],
        angles="xy", scale_units="xy", scale=1,
        color="#2ca02c", label=f"v1 + v2 = {v_sum}"
    )

    # Auto-scale limits with padding
    all_x = [0, v1[0], v_sum[0]]
    all_y = [0, v1[1], v_sum[1]]
    ax.set_xlim(min(all_x) - 2, max(all_x) + 2)
    ax.set_ylim(min(all_y) - 2, max(all_y) + 2)

    # Grid & Axis aesthetics
    ax.axhline(0, color="black", linewidth=1.2)
    ax.axvline(0, color="black", linewidth=1.2)
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_aspect("equal")
    ax.legend(loc="upper left")
    ax.set_title("3Blue1Brown Perspective: 2D Vector Addition (Tip-to-Tail)")

    # Save logic (Ensures 'assets' folder exists automatically)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    save_path = os.path.join(assets_dir, "vector_addition.png")
    plt.savefig(save_path, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    v1 = [3.0, 1.0]
    v2 = [1.0, 4.0]
    plot_vector_add(v1, v2)
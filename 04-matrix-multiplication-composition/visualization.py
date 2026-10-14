import os
import matplotlib.pyplot as plt

from matrix_from_scratch import matrix_multiply


def plot_matrix_composition(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> None:
    """Renders a 3-panel visualization illustrating matrix multiplication as composition."""
    matrix_c = matrix_multiply(matrix_a, matrix_b)

    i_hat = [1.0, 0.0]
    j_hat = [0.0, 1.0]

    b_i = [matrix_b[0][0], matrix_b[1][0]]
    b_j = [matrix_b[0][1], matrix_b[1][1]]

    c_i = [matrix_c[0][0], matrix_c[1][0]]
    c_j = [matrix_c[0][1], matrix_c[1][1]]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # --- Subplot 1: Transformation B ---
    ax1.quiver(0, 0, i_hat[0], i_hat[1], angles='xy', scale_units='xy', scale=1, color='gray', alpha=0.3, label='Original i-hat')
    ax1.quiver(0, 0, j_hat[0], j_hat[1], angles='xy', scale_units='xy', scale=1, color='lightgray', alpha=0.3, label='Original j-hat')
    ax1.quiver(0, 0, b_i[0], b_i[1], angles='xy', scale_units='xy', scale=1, color='#1f77b4', zorder=3, label=f'B(i-hat) = {b_i}')
    ax1.quiver(0, 0, b_j[0], b_j[1], angles='xy', scale_units='xy', scale=1, color='#ff7f0e', zorder=3, label=f'B(j-hat) = {b_j}')
    ax1.set_title("1. First Transformation (B)")

    # --- Subplot 2: Transformation A applied after B ---
    ax2.quiver(0, 0, b_i[0], b_i[1], angles='xy', scale_units='xy', scale=1, color='#1f77b4', alpha=0.4, label='Intermediate B(i)')
    ax2.quiver(0, 0, b_j[0], b_j[1], angles='xy', scale_units='xy', scale=1, color='#ff7f0e', alpha=0.4, label='Intermediate B(j)') 
    ax2.quiver(0, 0, c_i[0], c_i[1], angles='xy', scale_units='xy', scale=1, color='#2ca02c', zorder=3, label=f'A(B(i)) = {c_i}')
    ax2.quiver(0, 0, c_j[0], c_j[1], angles='xy', scale_units='xy', scale=1, color='#d62728', zorder=3, label=f'A(B(j)) = {c_j}')
    ax2.set_title("2. Second Transformation (A)")

    # --- Subplot 3: Direct Composite C = A * B ---
    ax3.quiver(0, 0, i_hat[0], i_hat[1], angles='xy', scale_units='xy', scale=1, color='gray', alpha=0.3, label='Original i-hat')
    ax3.quiver(0, 0, j_hat[0], j_hat[1], angles='xy', scale_units='xy', scale=1, color='lightgray', alpha=0.3, label='Original j-hat')
    ax3.quiver(0, 0, c_i[0], c_i[1], angles='xy', scale_units='xy', scale=1, color='#2ca02c', zorder=3, label=f'C(i-hat) = {c_i}')
    ax3.quiver(0, 0, c_j[0], c_j[1], angles='xy', scale_units='xy', scale=1, color='#d62728', zorder=3, label=f'C(j-hat) = {c_j}')
    ax3.set_title("3. Composite Transformation (C = A * B)")

    # Dynamic limits for consistent scaling across panels
    all_x = [0, i_hat[0], j_hat[0], b_i[0], b_j[0], c_i[0], c_j[0]]
    all_y = [0, i_hat[1], j_hat[1], b_i[1], b_j[1], c_i[1], c_j[1]]
    min_x, max_x = min(all_x) - 2, max(all_x) + 2
    min_y, max_y = min(all_y) - 2, max(all_y) + 2

    for ax in (ax1, ax2, ax3):
        ax.set_xlim(min_x, max_x)
        ax.set_ylim(min_y, max_y)
        ax.axhline(0, color='black', linewidth=1.2)
        ax.axvline(0, color='black', linewidth=1.2)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.set_aspect('equal')
        ax.legend(loc='upper left', framealpha=0.9)

    plt.tight_layout()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)

    plt.savefig(os.path.join(assets_dir, "matrix_composition.png"), bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    matrix_a = [[1.0, 1.0], [0.0, 1.0]]   # Shear
    matrix_b = [[0.0, -1.0], [1.0, 0.0]]  # 90° CCW Rotation

    plot_matrix_composition(matrix_a, matrix_b)
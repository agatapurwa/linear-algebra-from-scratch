import os
import matplotlib.pyplot as plt

from matrix_from_scratch import (
    matrix_vector_multiply,
    check_dimensionality_reduction,
    get_shear_horizontal_matrix
)


def plot_linear_transformation_comparison(
    v: list[float], 
    matrix_transform: list[list[float]], 
    matrix_collapse: list[list[float]]
) -> None:
    """Renders side-by-side visualizers for 2D Linear Transformations."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    i_hat = [1.0, 0.0]
    j_hat = [0.0, 1.0]

    # --- Subplot 1: Regular Linear Transformation (Shear) ---
    t_i_hat = [matrix_transform[0][0], matrix_transform[1][0]]
    t_j_hat = [matrix_transform[0][1], matrix_transform[1][1]]
    transformed_v = matrix_vector_multiply(matrix_transform, v)

    # Faded original vectors
    ax1.quiver(0, 0, i_hat[0], i_hat[1], angles='xy', scale_units='xy', scale=1, color='gray', alpha=0.3, label='Original i-hat')
    ax1.quiver(0, 0, j_hat[0], j_hat[1], angles='xy', scale_units='xy', scale=1, color='lightgray', alpha=0.3, label='Original j-hat')
    ax1.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='gray', linestyle='--', alpha=0.5, label=f'Original v = {v}')

    # Transformed vectors
    ax1.quiver(0, 0, t_i_hat[0], t_i_hat[1], angles='xy', scale_units='xy', scale=1, color='#1f77b4', zorder=3, label=f'Transformed i-hat = {t_i_hat}')
    ax1.quiver(0, 0, t_j_hat[0], t_j_hat[1], angles='xy', scale_units='xy', scale=1, color='#ff7f0e', zorder=3, label=f'Transformed j-hat = {t_j_hat}')
    ax1.quiver(0, 0, transformed_v[0], transformed_v[1], angles='xy', scale_units='xy', scale=1, color='#2ca02c', zorder=4, label=f'T(v) = {transformed_v}')

    # Dynamic limits (Handles negative values properly)
    all_x = [0, i_hat[0], j_hat[0], v[0], t_i_hat[0], t_j_hat[0], transformed_v[0]]
    all_y = [0, i_hat[1], j_hat[1], v[1], t_i_hat[1], t_j_hat[1], transformed_v[1]]
    ax1.set_xlim(min(all_x) - 2, max(all_x) + 2)
    ax1.set_ylim(min(all_y) - 2, max(all_y) + 2)

    ax1.axhline(0, color='black', linewidth=1.2)
    ax1.axvline(0, color='black', linewidth=1.2)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.set_aspect('equal')
    ax1.legend(loc='upper left', framealpha=0.9)
    ax1.set_title("1. 2D Linear Transformation (Shear)")


    # --- Subplot 2: Dimensionality Collapse (Det ≈ 0) ---
    c_i_hat = [matrix_collapse[0][0], matrix_collapse[1][0]]
    c_j_hat = [matrix_collapse[0][1], matrix_collapse[1][1]]

    # 1D Span Line
    span_scale = 3.0
    line_x = [-span_scale * c_i_hat[0], span_scale * c_i_hat[0]]
    line_y = [-span_scale * c_i_hat[1], span_scale * c_i_hat[1]]
    ax2.plot(line_x, line_y, color='purple', linestyle=':', linewidth=2, zorder=1, label='1D Span Line (Collapsed)')

    # Basis vector landings
    ax2.quiver(0, 0, c_i_hat[0], c_i_hat[1], angles='xy', scale_units='xy', scale=1, color='#1f77b4', width=0.012, zorder=3, label=f'Land i-hat = {c_i_hat}')
    ax2.quiver(0, 0, c_j_hat[0], c_j_hat[1], angles='xy', scale_units='xy', scale=1, color='#ff7f0e', width=0.008, zorder=2, label=f'Land j-hat = {c_j_hat}')

    max_val = max(abs(x) for x in c_i_hat + c_j_hat) * 2
    ax2.set_xlim(-max_val, max_val)
    ax2.set_ylim(-max_val, max_val)

    is_collapsed = check_dimensionality_reduction(matrix_collapse)
    ax2.set_title("2. Collapses to 1D Line (Det ≈ 0)" if is_collapsed else "2. Full 2D Space Preserved")

    ax2.axhline(0, color='black', linewidth=1.2)
    ax2.axvline(0, color='black', linewidth=1.2)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.set_aspect('equal')
    ax2.legend(loc='upper left', framealpha=0.9)


    # --- Save Output ---
    plt.tight_layout()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)

    plt.savefig(os.path.join(assets_dir, "linear_transformation.png"), bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    v = [2.0, 3.0]
    shear_matrix = get_shear_horizontal_matrix()
    collapse_matrix = [[1.0, 2.0], [2.0, 4.0]]

    plot_linear_transformation_comparison(v, shear_matrix, collapse_matrix)
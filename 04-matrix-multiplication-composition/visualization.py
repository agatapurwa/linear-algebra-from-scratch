import os
import matplotlib.pyplot as plt
# Import pure Python math function from first-principles script
from matrix_from_scratch import matrix_multiply

def plot_matrix_composition(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    """
    Renders a 3-panel visualization illustrating matrix multiplication as composition:
    - Subplot 1: Initial space vs First Transformation B (Rotation 90° CCW)
    - Subplot 2: Intermediate space vs Second Transformation A (Shear)
    - Subplot 3: Direct Composite Transformation C = A * B
    """
    # Compute composite matrix
    matrix_c = matrix_multiply(matrix_a, matrix_b)

    # Basis matrix
    i_hat = [1.0, 0.0]
    j_hat = [0.0, 1.0]

    # Transformed vectors after B (First transform)
    b_i_hat = [matrix_b[0][0], matrix_b[1][0]]
    b_i_hat = [matrix_b[0][1], matrix_b[1][1]]

    # Transformed vectors after A (Second transform applied on B's landing)
    final_i_hat = [matrix_c[0][0], matrix_c[1][0]]
    final_j_hat = [matrix_c[0][1], matrix_c[1][1]]

    # Initialize a 3-column subplot
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, fig_size=(18, 6))

    # subplot 1 
    # Original Basis (faded)
    ax1.quiver(0, 0, i_hat[0], i_hat[1], angles='xy', scale_units='xy', scale=1, color='gray', alpha=0.3, label='Original i-hat')
    ax1.quiver(0, 0, j_hat[0], j_hat[1], angles='xy', scale_units='xy', scale=1, color='lightgray', alpha=0.3, label='Original j-hat')

    # After Matrix B
    ax1.quiver(0, 0, b_i_hat[0], b_i_hat[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original i-hat')

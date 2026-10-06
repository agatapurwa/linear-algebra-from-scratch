import os
import matplotlib.pyplot as plt

# Import pure Python math functions from first-principles script
from matrix_from_scratch import (
    scalar_multiplication, 
    linear_combination, 
    check_linear_depedance, 
    generate_span_sample
)

def plot_combined_visualizations(v1: list[float], v2: list[float], c1: float, c2: float) -> None:
    """
    Renders a side-by-side visualization comparing a single linear combination (Tip-to-Tail)
    against the full 2D vector span grid.

    Args:
        v1: First input vector [x, y]
        v2: Second input vector [x, y]
        c1: Scalar constant for v1
        c2: Scalar constant for v2
    """
    # 1. Input Validation
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError(f"Both vectors must be 2D. Received len(v1)={len(v1)}, len(v2)={len(v2)}")

    # 2. Initialize Canvas with 2 Subplots (1 Row, 2 Columns)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # ==========================================
    # SUBPLOT 1: SPECIFIC LINEAR COMBINATION
    # ==========================================
    scaled_v1 = scalar_multiplication(v1, c1)
    scaled_v2 = scalar_multiplication(v2, c2)
    v_result = linear_combination([v1, v2], [c1, c2])

    # Draw c1*v1 from Origin (0,0)
    ax1.quiver(0, 0, scaled_v1[0], scaled_v1[1], angles='xy', scale_units='xy', scale=1, 
               color='#1f77b4', label=f'{c1}v1 = {scaled_v1}')
    
    # Draw c2*v2 from the Tip of scaled_v1
    ax1.quiver(scaled_v1[0], scaled_v1[1], scaled_v2[0], scaled_v2[1], angles='xy', scale_units='xy', scale=1, 
               color='#ff7f0e', label=f'{c2}v2 = {scaled_v2} (Tip-to-Tail)')
    
    # Draw Resultant Vector from Origin
    ax1.quiver(0, 0, v_result[0], v_result[1], angles='xy', scale_units='xy', scale=1, 
               color='#2ca02c', label=f'v_result = {v_result}')

    # Plot Configuration (Subplot 1)
    all_x = [0, scaled_v1[0], v_result[0]]
    all_y = [0, scaled_v1[1], v_result[1]]
    padding = 2.0
    ax1.set_xlim(min(all_x) - padding, max(all_x) + padding)
    ax1.set_ylim(min(all_y) - padding, max(all_y) + padding)
    ax1.axhline(0, color='black', linewidth=1.2)
    ax1.axvline(0, color='black', linewidth=1.2)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.set_aspect('equal')
    ax1.legend(loc='upper left')
    ax1.set_title(f"Linear Combination: {c1}*v1 + {c2}*v2")

    # ==========================================
    # SUBPLOT 2: VECTOR SPAN VISUALIZATION
    # ==========================================
    c_values = [i * 0.5 for i in range(-6, 7)]
    span_points = generate_span_sample(v1, v2, c_values)
    x_pts = [pt[0] for pt in span_points]
    y_pts = [pt[1] for pt in span_points]

    # Draw Span Sample Points
    ax2.scatter(x_pts, y_pts, color='gray', alpha=0.4, s=20, label='Span (Linear Combination Grid)')

    # Draw Input Vectors v1 and v2
    ax2.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, 
               color='blue', label=f'v1 = {v1}')
    ax2.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, 
               color='orange', label=f'v2 = {v2}')

    # Evaluate Span Dimension
    is_dependent = check_linear_depedance(v1, v2)
    title_span = "Span from Dependent Vectors (1D Line)" if is_dependent else "Span from Independent Vectors (Full 2D Plane)"

    # Plot Configuration (Subplot 2)
    ax2.axhline(0, color='black', linewidth=1.2)
    ax2.axvline(0, color='black', linewidth=1.2)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.set_aspect('equal')
    ax2.legend(loc='upper left')
    ax2.set_title(title_span)

    # ==========================================
    # FILE EXPORT & RENDERING
    # ==========================================
    plt.tight_layout()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)
    
    output_path = os.path.join(assets_dir, "combined_linear_algebra.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    v1 = [3.0, 1.0]
    v2 = [1.0, 2.0]
    c1 = 2.0
    c2 = -1.5

    plot_combined_visualizations(v1, v2, c1, c2)
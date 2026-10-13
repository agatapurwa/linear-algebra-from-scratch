import os
import matplotlib.pyplot as plt

# Import pure Python math functions from first-principles script
from matrix_from_scratch import (
    scalar_multiplication, 
    linear_combination, 
    check_linear_dependence,  # TYPO from check_linear_depedence
    generate_span_sample
)

def plot_combined_visualizations(v1: list[float], v2: list[float], c1: float, c2: float) -> None:
    """Renders a side-by-side visualization of a linear combination and a vector span grid."""
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError(f"Both vectors must be 2D. Received {len(v1)} and {len(v2)}")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # --- Subplot 1: Linear Combination ---
    scaled_v1 = scalar_multiplication(v1, c1)
    scaled_v2 = scalar_multiplication(v2, c2)
    v_result = linear_combination([v1, v2], [c1, c2])

    ax1.quiver(0, 0, scaled_v1[0], scaled_v1[1], angles='xy', scale_units='xy', scale=1, 
               color='#1f77b4', label=f'{c1}v1 = {scaled_v1}')
    
    ax1.quiver(scaled_v1[0], scaled_v1[1], scaled_v2[0], scaled_v2[1], angles='xy', scale_units='xy', scale=1, 
               color='#ff7f0e', label=f'{c2}v2 = {scaled_v2} (Tip-to-Tail)')
    
    ax1.quiver(0, 0, v_result[0], v_result[1], angles='xy', scale_units='xy', scale=1, 
               color='#2ca02c', label=f'Result = {v_result}')

    all_x = [0, scaled_v1[0], v_result[0]]
    all_y = [0, scaled_v1[1], v_result[1]]
    ax1.set_xlim(min(all_x) - 2, max(all_x) + 2)
    ax1.set_ylim(min(all_y) - 2, max(all_y) + 2)
    
    ax1.axhline(0, color='black', linewidth=1.2)
    ax1.axvline(0, color='black', linewidth=1.2)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.set_aspect('equal')
    ax1.legend(loc='upper left')
    ax1.set_title(f"Linear Combination: {c1}*v1 + {c2}*v2")


    # --- Subplot 2: Vector Span ---
    c_values = [i * 0.5 for i in range(-6, 7)]
    span_points = generate_span_sample(v1, v2, c_values)
    
    # MAGIC TRICK: Unpacking list of coordinates in one line
    x_pts, y_pts = zip(*span_points)

    ax2.scatter(x_pts, y_pts, color='gray', alpha=0.4, s=20, label='Span Grid')
    ax2.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label=f'v1 = {v1}')
    ax2.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='orange', label=f'v2 = {v2}')

    is_dependent = check_linear_dependence(v1, v2)
    ax2.set_title("Span: Dependent (1D Line)" if is_dependent else "Span: Independent (Full 2D Plane)")

    ax2.axhline(0, color='black', linewidth=1.2)
    ax2.axvline(0, color='black', linewidth=1.2)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.set_aspect('equal')
    ax2.legend(loc='upper left')


    # --- Export & Rendering ---
    plt.tight_layout()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)
    
    plt.savefig(os.path.join(assets_dir, "combined_linear_algebra.png"), bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    plot_combined_visualizations(v1=[3.0, 1.0], v2=[1.0, 2.0], c1=2.0, c2=-1.5)
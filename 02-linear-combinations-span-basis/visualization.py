import os
import matplotlib.pyplot as plt

# Import your pure python function from your math file
from matrix_from_scratch import scalar_multiplication, linear_combination, check_linear_depedance

def plot_linear_combination(v1: list[float], v2: list[float], c1: float, c2: float) -> None:
    """
    Plots two 2D basis/input vectors, their scaled components, and the
    resulting linear combination vector v_result = c1*v1 + c2*v2.

    Args:
    v1: First basis vector [x, y]
    v2: Second basis vector [x, y]
    c1: Scalar for v1
    c2: Scalar for v2
    """

    # PSEUDO-CODE / GUIDE:
    #1. Check that v1 and v2 are 2D vectors. If not, raise ValueError.
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError(f"Both vectors must be 2D. Received len(v1)={len(v1)}, len(v2)={len(v2)}")

    #2. Compute scaled vectors and the final linear combination:
    scaled_v1 = scalar_multiplication(v1, c1)
    scaled_v2 = scalar_multiplication(v2, c2)
    v_result  = linear_combination([v1, v2], [c1, c2])

    #3. Initialize Matplotlib plot canvas:
    fig, ax= plt.subplots(figsize=(8, 8))

    #4. Draw Scaled Vector 1 (c1*v1) starting from origin (0, 0):
    ax.quiver(0,
              0,
              scaled_v1[0],
              scaled_v1[1],
              angles='xy',
              scale_units='xy',
              scale=1,
              color='#1f77b4',
              label=f'{c1}v1 = {scaled_v1}'
              )

    #5. Draw Vector 2 (c2, v2) starting from the TIP of scaled_vector1 (scaled_v1[0], scaled_v2[1]):
    ax.quiver(scaled_v1[0],
              scaled_v1[1],
              scaled_v2[0],
              scaled_v2[1],
              angles='xy',
              scale_units='xy',
              scale=1,
              color='#ff7f0e',
              label=f'{c2}v2 = {scaled_v2}(Tip-to-Tail)'
             )

    #6. Draw Resultant Vector (v_result = c1*v1 + c2*v2) from Origin (0,0):
    ax.quiver(0,
              0,
              v_result[0],
              v_result[1],
              angles='xy',
              scale_units='xy',
              scale=1,
              color='#2ca02c',
              label=f'v_result = {v_result}'
              )

    #7. Configure Grid, Limits, and Labels:
    #    Calculate min and max bounds based on origin, scaled_v1, and v_result plus padding (+2/-2).
    all_x = [0, scaled_v1[0], v_result[0]]
    all_y = [0, scaled_v1[1], v_result[1]]

    padding = 2.0
    min_x, max_x = min(all_x) - padding, max(all_x) + padding
    min_y, max_y = min(all_y) - padding, max(all_y) + padding
    
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)
    ax.axhline(0, color='black', linewidth=1.2) #x-axis line
    ax.axvline(0, color='black', linewidth=1.2) 
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_aspect('equal')
    ax.legend(loc='upper left')
    ax.set_title(f"Linear Combination: {c1}*v1 + {c2}*v2")

    #8. Safe File Saving (Robust Path Handling):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)

    output_path = os.path.join(assets_dir, "linear_combination.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Standard basis vectors î = [1, 0], ĵ = [0, 1] or custom 2D vectors
    v1 = [3.0, 1.0]
    v2 = [1.0, 2.0]
    c1 = 2.0
    c2 = -1.5

    plot_linear_combination(v1, v2, c1, c2)
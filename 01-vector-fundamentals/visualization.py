import os
import matplotlib.pyplot as plt

# Import your pure Python function from your math file
from matrix_from_scratch import vector_add

def plot_vector_add(v1: list[float], v2: list[float]) -> None:
    """
    Plots two 2D vectors and their tip-to-tail sum on a Cartesian grid.

    Args:
        v1: Base vector [x, y] starting at origin [0, 0].
        v2: Second vector [x, y] placed at the tip of v1.
    """
    # PSEUDO-CODE / GUIDE:
    # 1. Check if both vectors are 2D (len == 2). If not, raise ValueError("Only 2D vectors supported for this plot").
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError ("Only 2D vectors are supported for this visual plot.")
    
    # 2. Compute the resultant vector sum using your custom vector_add(v1, v2):
    #    - v_sum = vector_add(v1, v2)
    v_sum = vector_add(v1, v2)

    # 3. Initialize matplotlib plot canvas:
    #    - fig, ax = plt.subplots(figsize=(8, 8))
    fig, ax = plt.subplots(figsize=(8, 8))

    # 4. Draw Vector 1 (v1) starting from Origin (0, 0):
    #    - Use ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
    ax.quiver(0,
              0,
              v1[0],
              v1[1], 
              angles='xy',
              scale_units='xy',
              scale=1,
              color='#1f77b4',
              label=f'v1 = {v1}',
              )

    # 5. Draw Vector 2 (v2) starting from the TIP of v1 (v1[0], v1[1]):
    #    - Start x = v1[0], Start y = v1[1]
    #    - Displacement x = v2[0], Displacement y = v2[1]
    #    - Use ax.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='orange', label='v2 (Tip-to-Tail)')
    ax.quiver(v1[0],
              v1[1],
              v2[0],
              v2[1],
              angles='xy',
              scale_units='xy',
              scale=1,
              color='#ff7f0e',
              label=f'v2 = {v2} (Tip-to-Tail)',
    )

    # 6. Draw Resultant Vector (v1 + v2) starting from Origin (0, 0):
    #    - Start x = 0, Start y = 0
    #    - End point = v_sum[0], v_sum[1]
    #    - Use ax.quiver(0, 0, v_sum[0], v_sum[1], angles='xy', scale_units='xy', scale=1, color='green', label='v1 + v2')
    ax.quiver(0,
              0,
              v_sum[0],
              v_sum[1],
              angles='xy',
              scale_units='xy',
              scale=1,
              color='#2ca02c',
              label=f'v1 + v2 = {v_sum}',
    )

    # 7. Configure Grid and Axes Limits:
    #    - Compute max bounds so all vectors fit on screen:
    #      max_x = max(0, v1[0], v_sum[0]) + 2
    #      max_y = max(0, v1[1], v_sum[0]) + 2
    #    - ax.set_xlim(-2, max_x)
    #    - ax.set_ylim(-2, max_y)
    #    - ax.axhline(0, color='black', linewidth=1)  # X-axis line
    #    - ax.axvline(0, color='black', linewidth=1)  # Y-axis line
    #    - ax.grid(True, linestyle='--', alpha=0.6)
    #    - ax.legend()
    #    - ax.set_title("3Blue1Brown Perspective: 2D Vector Addition (Tip-to-Tail)")
    all_x = [0, v1[0], v_sum[0]]
    all_y = [0, v1[1], v_sum[1]] 

    min_x, max_x = min(all_x) - 2, max(all_x) + 2
    min_y, max_y = min(all_y) - 2, max(all_y) + 2

    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)
    ax.axhline(0, color="black", linewidth=1.2)  # X-axis line
    ax.axvline(0, color="black", linewidth=1.2)  # Y-axis line
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_aspect("equal")  # Ensures 1 unit along X equals 1 unit along Y
    ax.legend(loc="upper left")
    ax.set_title("3Blue1Brown Perspective: 2D Vector Addition (Tip-to-Tail)")
    
    # 8. Save and Render figure:
    # Get the directory where the visualization.py file is located.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, "assets", "vector_addition.png")
    plt.savefig(save_path, bbox_inches='tight')

    #    - plt.show()
    plt.show()

if __name__ == "__main__":
    # Test vectors
    v1=  [3.0, 1.0]
    v2 = [1.0, 4.0]

    plot_vector_add(v1, v2)


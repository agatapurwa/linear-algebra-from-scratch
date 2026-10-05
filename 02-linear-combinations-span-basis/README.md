# 02. Linear Combinations, Span & Basis Vectors

This module implements core linear algebra concepts—scalar multiplication, linear combinations, and linear dependence testing—from first principles using standard Python data structures (`list[float]`) without relying on external numerical acceleration libraries like NumPy. It also includes a 2D geometric visualizer inspired by 3Blue1Brown's *Essence of Linear Algebra*.

## 📌 Implemented Core Concepts

### 1. Scalar Multiplication (`scalar_multiplication`)

* **Mathematical Concept:** Scales each component of a vector by a scalar constant $c$.
* **Geometric View:** Stretches, compresses, or reverses the direction of a vector without altering its span line.
* **Formula:**

$$c \cdot \vec{v} = [c \cdot v_1, c \cdot v_2, \dots, c \cdot v_n]$$



### 2. Vector Addition (`vector_add`)

* **Mathematical Concept:** Component-wise sum of two equal-dimensional vectors $\vec{v}_1, \vec{v}_2 \in \mathbb{R}^n$.
* **Safety:** Enforces strict dimension checking, throwing a `ValueError` if vector lengths do not match.
* **Formula:**

$$\vec{v}_1 + \vec{v}_2 = [v_{1,1} + v_{2,1}, v_{1,2} + v_{2,2}]$$



### 3. Linear Combination (`linear_combination`)

* **Mathematical Concept:** Computes the weighted sum of $N$ vectors scaled by $N$ scalar coefficients.
* **Algorithm:** Validates array lengths and vector dimensions, initializes a zero vector of corresponding dimension, and iteratively accumulates scaled vector components.
* **Formula:**

$$\vec{v}_{\text{result}} = c_1 \vec{v}_1 + c_2 \vec{v}_2 + \dots + c_n \vec{v}_n = \sum_{i=1}^{n} c_i \vec{v}_i$$



### 4. Linear Dependence Check (`check_linear_dependance`)

* **Mathematical Concept:** Determines whether two 2D vectors are linearly dependent (collinear/parallel) by evaluating their 2D determinant (cross product).
* **Numerical Safety:** Uses a floating-point tolerance threshold ($\epsilon = 10^{-9}$) to account for precision limits.
* **Formula:**

$$\det([\vec{v}_1 \quad \vec{v}_2]) = v_{1,1} v_{2,2} - v_{1,2} v_{2,1}$$


$$\text{If } \vert{}\det\vert{} < 10^{-9} \implies \text{Linearly Dependent}$$



### 5. 2D Linear Combination Visualizer (`visualization.py`)

* Renders 2D basis/input vectors, their scaled components, and the resulting linear combination vector using `matplotlib.quiver`.
* Graphically illustrates the Tip-to-Tail property of vector linear combinations:
* Scaled vector $c_1 \vec{v}_1$ originates from the origin $(0,0)$.
* Scaled vector $c_2 \vec{v}_2$ originates at the tip of $c_1 \vec{v}_1$.
* Resultant vector $\vec{v}_{\text{result}} = c_1 \vec{v}_1 + c_2 \vec{v}_2$ spans directly from $(0,0)$ to the tip of $c_2 \vec{v}_2$.


* Automatically manages output directory creation and saves high-resolution plot assets under `assets/linear_combination.png`.

---

## 📂 File Structure

```text
02-linear-combinations-span-basis/
├── assets/
│   └── linear_combination.png  # Rendered plot asset
├── README.md                   # Folder-level documentation and concept guide
├── matrix_from_scratch.py      # First-principles math implementations (pure Python)
└── visualization.py            # 2D Matplotlib visualizer

```

---

## 🚀 How to Run

### 1. Test Core Operations

Run `matrix_from_scratch.py` to execute built-in unit tests for scalar multiplication, vector addition, and linear combinations:

```bash
python matrix_from_scratch.py

```

**Expected Output:**

```text
=== MATRIX & VECTOR OPERATIONS TEST ===
Scalar Multiplication (2.0 * [3.0, 1.0]) : [6.0, 2.0]
Vector Addition ([3.0, 1.0] + [1.0, 2.0])        : [4.0, 3.0]
Linear Combination (2.0*v1 + -1.5*v2) : [4.5, -1.0]

```

### 2. Render Vector Visualization

Run `visualization.py` to generate and display the interactive plot:

```bash
python visualization.py

```

---

## 🖼️ Geometric Visualization

Here is the 2D Tip-to-Tail linear combination rendered using Matplotlib:

![2D Linear Combination](assets\linear_combination.png)
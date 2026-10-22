# Linear Algebra from Scratch

A pure Python, zero-dependency implementation of foundational linear algebra concepts, geometric transformations, and visual intuitions inspired by 3Blue1Brown's *Essence of Linear Algebra*.

---

## 📌 Architectural Evolution: Procedural to OOP

This repository intentionally documents a dual-phase software engineering journey, demonstrating how mathematical logic evolves from low-level algorithms into an extensible software engine.

* **Modules 01–05 (Functional & Procedural Phase)**: Focuses on pure mathematical mechanics, raw index manipulation, and explicit vector/matrix arithmetic using standard Python primitives (`list[float]`). This transparent approach exposes underlying computations without premature abstraction.
* **Modules 06+ (Object-Oriented Refactoring Phase)**: Introduces a Pythonic linear algebra engine built with custom classes (`Vector`, `Matrix`). It leverages dunder methods (`__matmul__`, `__add__`, `__repr__`) for natural mathematical syntax ($A @ B$, $v_1 + v_2$), `@property` decorators, and encapsulated matrix operations.

---

## 🗺️ Learning Roadmap

| Module | Core Concepts | Architectural Paradigm | Visual Output | Status |
| --- | --- | --- | --- | --- |
| **01-vector-fundamentals** | Vector addition, scalar multiplication, $\mathbb{R}^2$ space mechanics | Procedural | `vector_addition.png` | ✅ Complete |
| **02-linear-combinations-span-basis** | Linear independence, span, standard basis vectors ($\hat{i}, \hat{j}$) | Procedural | `combined_linear_algebra.png` | ✅ Complete |
| **03-linear-transformation-matrices** | Matrix-vector multiplication, 2D spatial transformations | Procedural | `linear_transformation.png` | ✅ Complete |
| **04-matrix-multiplication-composition** | Matrix composition, sequential spatial transformations | Procedural | `matrix_composition.png` | ✅ Complete |
| **05-three-dimensional-transformations** | 3D basis transformations ($\hat{i}, \hat{j}, \hat{k}$), $3 \times 3$ matrix operations, Y-axis rotation | Procedural | `3d_linear_transformation.png` | ✅ Complete |
| **06-the-determinant** | Area/volume scaling factor, dimensional collapse ($\det = 0$), orientation flip | OOP (`Matrix` Class) | `determinant_scaling.png` | ✅ Complete |
| **07-inverse-matrices-column-null-space** | Inverse matrice ($\mathbb{A}^-1$), Column space, Null space | OOP (`Matrix` Class) | `linear_system_inverse.png` | 🔄 In Progress |

---

## 📁 Repository Structure

```text
linear-algebra-from-scratch/
├── 01-vector-fundamentals/
│   ├── assets/
│   │   └── vector_addition.png
│   ├── matrix_from_scratch.py
│   ├── visualization.py
│   └── README.md
├── 02-linear-combinations-span-basis/
│   ├── assets/
│   │   └── combined_linear_algebra.png
│   ├── matrix_from_scratch.py
│   ├── visualization.py
│   └── README.md
├── 03-linear-transformation-matrices/
│   ├── assets/
│   │   └── linear_transformation.png
│   ├── matrix_from_scratch.py
│   ├── visualization.py
│   └── README.md
├── 04-matrix-multiplication-composition/
│   ├── assets/
│   │   └── matrix_composition.png
│   ├── matrix_from_scratch.py
│   ├── visualization.py
│   └── README.md
├── 05-three-dimensional-transformations/
│   ├── assets/
│   │   └── 3d_linear_transformation.png
│   ├── matrix_from_scratch.py
│   ├── visualization.py
│   └── README.md
├── 06-the-determinant/
│   ├── assets/
│   │   └── determinant_scaling.png
│   ├── matrix_from_scratch.py
│   ├── visualization.py
│   └── README.md
├── .gitignore
└── README.md

```

---

## 🚀 Getting Started

### 1. Prerequisites & Environment Setup

Clone the repository and set up your Python virtual environment:

```bash
git clone https://github.com/your-username/linear-algebra-from-scratch.git
cd linear-algebra-from-scratch
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install matplotlib

```

### 2. Running Modules

Each module is self-contained and can be executed independently from the root directory:

```bash
# Execute Module 05 Math Logic
python 05-three-dimensional-transformations/matrix_from_scratch.py

# Launch 3D Interactive Visualizer & Export Plot Asset
python 05-three-dimensional-transformations/visualization.py

```

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.
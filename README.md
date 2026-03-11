# 42 Matrix — Linear Algebra in Python

A complete implementation of linear algebra primitives, from basic vector operations to advanced matrix decompositions. All classes live in [`linear_algebra.py`](linear_algebra.py); each exercise file imports from it and demonstrates the new concept.

---

## Project Structure

```
linear_algebra.py          ← single source of truth for Vector and Matrix
ex00_add_subtract_scale.py ← vector/matrix add, sub, scale
ex01_linear_combination.py ← linear combination of vectors
ex02_linear_interpolation.py ← lerp for scalars, vectors, matrices
ex03_dot_product.py        ← dot product
ex04_norm.py               ← L1, L2, L∞ norms
ex05_cosine.py             ← cosine similarity
ex06_cross_product.py      ← 3D cross product
ex07_linear_map.py         ← matrix × vector, matrix × matrix
ex08_trace.py              ← trace (sum of diagonal)
ex09_transpose.py          ← matrix transpose
ex10_row_echelon_form.py   ← Gaussian elimination → row echelon form
ex11_determinant.py        ← determinant via row echelon
ex12_inverse.py            ← inverse via Gauss-Jordan
ex13_rank.py               ← rank via row echelon
```

---

## Exercise 00 — Vector & Matrix: The Container

### Concept
Before doing math, we need data structures. A **Vector** is a 1D ordered list of numbers representing a point or direction in space. A **Matrix** is a 2D grid of numbers representing a linear transformation (rotation, scaling, shearing, …).

### Examples
```python
u = Vector([2.0, 3.0])
v = Vector([5.0, 7.0])
u.add(v)   # Vector([7.0, 10.0])
u.sub(v)   # Vector([-3.0, -4.0])
u.scl(2.0) # Vector([4.0, 6.0])

A = Matrix([[1.0, 2.0], [3.0, 4.0]])
B = Matrix([[7.0, 4.0], [-2.0, 2.0]])
A.add(B)   # Matrix([[8.0, 6.0], [1.0, 6.0]])
A.scl(0.5) # Matrix([[0.5, 1.0], [1.5, 2.0]])
```

### Key Design Decision
All values are cast to `float` on construction — linear algebra requires floating-point precision. The `shape` attribute is stored eagerly so it does not need recomputing on every operation.

---

## Exercise 01 — Linear Combination

### Concept
A **linear combination** takes a list of vectors and a matching list of scalars (coefficients), scales each vector, and sums the results.

```
result = c₀·u₀ + c₁·u₁ + … + cₙ·uₙ
```

This is the core idea of **vector spaces**: if you can reach every point in a space by combining a set of vectors, those vectors *span* the space.


### Examples
```python
e1 = Vector([1.0, 0.0, 0.0])
e2 = Vector([0.0, 1.0, 0.0])
e3 = Vector([0.0, 0.0, 1.0])

linear_combination([e1, e2, e3], [10.0, -2.0, 0.5])
# Vector([10.0, -2.0, 0.5])
# → 10*e1 + (-2)*e2 + 0.5*e3

v1 = Vector([1.0, 2.0, 3.0])
v2 = Vector([0.0, 10.0, -100.0])
linear_combination([v1, v2], [10.0, -2.0])
# Vector([10.0, 0.0, 230.0])
# → 10*[1,2,3] + (-2)*[0,10,-100] = [10,20,30] + [0,-20,200]
```

### Why It Matters
Any matrix–vector product `Av` is a linear combination of the columns of `A`, using the entries of `v` as coefficients.

---

## Exercise 02 — Linear Interpolation (Lerp)

### Concept
Lerp smoothly blends between two values at a fractional position `t ∈ [0, 1]`.

```
lerp(u, v, t) = u + t·(v − u)   equivalent to   (1−t)·u + t·v
```

- `t = 0` → returns `u` exactly
- `t = 1` → returns `v` exactly
- `t = 0.5` → returns the midpoint

Works on scalars, Vectors, and Matrices.

### Examples
```python
lerp(0.0, 10.0, 0.0)   # 0.0    (start)
lerp(0.0, 10.0, 1.0)   # 10.0   (end)
lerp(0.0, 10.0, 0.5)   # 5.0    (midpoint)
lerp(21.0, 42.0, 0.3)  # 27.3

lerp(Vector([2.0, 1.0]), Vector([4.0, 2.0]), 0.3)
# Vector([2.6, 1.3])   → [2,1] + 0.3*([4,2]-[2,1])

lerp(Matrix([[2.0, 1.0], [3.0, 4.0]]),
     Matrix([[20.0, 10.0], [30.0, 40.0]]), 0.5)
# Matrix([[11.0, 5.5], [16.5, 22.0]])
```

### Real-World Uses
Animation (smooth movement between keyframes), color blending, camera paths, physics simulation.

---

## Exercise 03 — Dot Product

### Concept
The **dot product** collapses two vectors into a single scalar representing their "overlap":

```
u · v = Σ uᵢ·vᵢ
```

| Result | Meaning |
|---|---|
| > 0 | vectors point in the same general direction (angle < 90°) |
| = 0 | vectors are perpendicular (orthogonal) |
| < 0 | vectors point in opposite general directions (angle > 90°) |

### Examples
```python
Vector([0.0, 0.0]).dot(Vector([1.0, 1.0]))   # 0.0  (zero vector)
Vector([1.0, 1.0]).dot(Vector([1.0, 1.0]))   # 2.0
Vector([-1.0, 6.0]).dot(Vector([3.0, 2.0]))  # 9.0  → (-1)*3 + 6*2
Vector([1.0, 0.0]).dot(Vector([0.0, 1.0]))   # 0.0  (perpendicular)
```

---

## Exercise 04 — Norms (L1, L2, L∞)

### Concept
A **norm** measures the "size" or "length" of a vector. Three common norms:

| Norm | Formula | Intuition |
|---|---|---|
| L1 (Manhattan) | `‖u‖₁ = Σ |uᵢ|` | distance walking along city grid blocks |
| L2 (Euclidean) | `‖u‖₂ = √(Σ uᵢ²)` | straight-line distance in space |
| L∞ (Supremum) | `‖u‖∞ = max(|uᵢ|)` | the single most extreme coordinate |

### Examples
```python
u = Vector([3.0, -4.0])
u.norm_1()    # 7.0   → |3| + |-4|
u.norm()      # 5.0   → √(9 + 16)
u.norm_inf()  # 4.0   → max(3, 4)

u = Vector([1.0, 2.0, 3.0])
u.norm_1()    # 6.0
u.norm()      # 3.7416…  → √14
u.norm_inf()  # 3.0
```

### When to Use Which
- **L2**: physics distances, nearest-neighbor search
- **L1**: sparse models (LASSO regression), robust statistics
- **L∞**: bounding boxes, Chebyshev distance in chess

---

## Exercise 05 — Cosine Similarity

### Concept
Measures the **angle** between two vectors, ignoring their magnitudes:

```
cos(θ) = (u · v) / (‖u‖₂ · ‖v‖₂)
```

Result is always in `[-1, 1]`:
- `1.0` → same direction (parallel)
- `0.0` → perpendicular
- `-1.0` → opposite directions

### Examples
```python
angle_cos(Vector([1., 0.]), Vector([1., 0.]))   # 1.0   (same direction)
angle_cos(Vector([1., 0.]), Vector([0., 1.]))   # 0.0   (perpendicular)
angle_cos(Vector([-1., 1.]), Vector([1., -1.])) # -1.0  (opposite)
angle_cos(Vector([2., 1.]), Vector([4., 2.]))   # 1.0   (same direction, different length)
angle_cos(Vector([1., 2., 3.]), Vector([4., 5., 6.]))  # 0.9746…
```

### Key Insight
`Vector([2, 1])` and `Vector([4, 2])` point in exactly the same direction — cosine similarity returns `1.0` regardless of scale. This is why it's used in NLP (comparing word embeddings) and recommendation systems.

---

## Exercise 06 — Cross Product

### Concept
**Only for 3D vectors.** Produces a new vector that is perpendicular to both inputs:

```
u × v = ( u_y·v_z − u_z·v_y,
           u_z·v_x − u_x·v_z,
           u_x·v_y − u_y·v_x )
```

The magnitude `‖u × v‖` equals the area of the parallelogram spanned by `u` and `v`. Direction follows the **right-hand rule**.

### Examples
```python
# Canonical basis vectors
cross_product(Vector([0., 0., 1.]), Vector([1., 0., 0.]))
# Vector([0., 1., 0.])   → Z × X = Y

cross_product(Vector([1., 2., 3.]), Vector([4., 5., 6.]))
# Vector([-3., 6., -3.])

cross_product(Vector([4., 2., -3.]), Vector([-2., -5., 16.]))
# Vector([17., -58., -16.])
```

### Real-World Uses
3D graphics (surface normals for lighting), physics (torque = r × F), robotics (rotation axes).

---

## Exercise 07 — Matrix–Vector and Matrix–Matrix Multiplication

### Concept
**Matrix–vector** (`mul_vec`): applies a linear transformation to a vector.
```
(Av)ᵢ = Σⱼ Aᵢⱼ · vⱼ    (dot product of row i with v)
```

**Matrix–matrix** (`mul_mat`): composes two transformations.
```
Cᵢⱼ = Σₖ Aᵢₖ · Bₖⱼ    (A must be m×n, B must be n×p → C is m×p)
```

### Examples
```python
# Identity × v = v
Matrix([[1., 0.], [0., 1.]]).mul_vec(Vector([4., 2.]))
# Vector([4.0, 2.0])

# Scale by 2
Matrix([[2., 0.], [0., 2.]]).mul_vec(Vector([4., 2.]))
# Vector([8.0, 4.0])

# Reflection about y=x line (swap components)
Matrix([[0., 1.], [1., 0.]]).mul_vec(Vector([3., 7.]))
# Vector([7.0, 3.0])

# Identity × Identity = Identity
I = Matrix([[1., 0.], [0., 1.]])
I.mul_mat(I)
# Matrix([[1.0, 0.0], [0.0, 1.0]])

# Combining two transformations
Matrix([[1., 0.], [0., 1.]]).mul_mat(Matrix([[2., 1.], [4., 2.]]))
# Matrix([[2.0, 1.0], [4.0, 2.0]])
```

---

## Exercise 08 — Trace

### Concept
Sum of the **diagonal** elements of a square matrix:

```
tr(A) = Σᵢ Aᵢᵢ
```

### Examples
```python
Matrix([[1., 0.], [0., 1.]]).trace()              # 2.0  (identity)
Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]]).trace()  # 9.0  (2+3+4)
Matrix([[-2., -8., 4.], [1., -23., 4.], [0., 6., 4.]]).trace() # -21.0
```

### Why It Matters
- The trace is **invariant under change of basis**: `tr(A) = tr(PAPˉ¹)` for any invertible P.
- It equals the **sum of eigenvalues** of A.
- In physics, the trace of a stress tensor equals the total pressure.

---

## Exercise 09 — Transpose

### Concept
Flip the matrix over its main diagonal — rows become columns:

```
(Aᵀ)ᵢⱼ = Aⱼᵢ
```

A matrix of shape `(m, n)` becomes shape `(n, m)`.

### Examples
```python
u = Matrix([[1., 2., 3.], [4., 5., 6.]])   # shape (2, 3)
u.transpose()
# Matrix([[1., 4.], [2., 5.], [3., 6.]])   shape (3, 2)

u = Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]])  # square (3,3)
u.transpose()
# Matrix([[2., 4., -2.], [-5., 3., 3.], [0., 7., 4.]])
```

### Key Properties
- `(Aᵀ)ᵀ = A`
- `(AB)ᵀ = BᵀAᵀ` (order reverses)
- Used in: least squares (`AᵀA`x = `Aᵀb`), dot product as matrix product (`uᵀv`), symmetric matrices (`A = Aᵀ`)

---

## Exercise 10 — Row Echelon Form (REF)

### Concept
Transform a matrix to **upper-triangular** shape using row operations, so all entries below each pivot are zero. Uses **Gaussian elimination with partial pivoting**.

**Algorithm:**
1. For each column `j`, find the row `≥ pivot_row` with the largest `|value|` (partial pivot).
2. Swap it into `pivot_row` (count the swap for determinant sign).
3. Eliminate all rows below: `rowᵢ -= (Aᵢⱼ / A_pivot_j) * pivot_row`
4. Advance `pivot_row`.

### Examples
```python
Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).row_echelon()
# Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]), swaps=0

Matrix([[1., 2.], [3., 4.]]).row_echelon()
# Matrix([[3., 4.], [0., 0.666…]]), swaps=1  (pivot: row with |3| > |1|)

Matrix([[1., 2.], [2., 4.]]).row_echelon()
# Matrix([[2., 4.], [0., 0.]]), swaps=1      (rank-deficient: rows are multiples)

Matrix([[8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.]]).row_echelon()
# Upper triangular with zeros below each pivot
```

### Why Partial Pivoting?
Choosing the largest pivot prevents division by near-zero values, reducing floating-point rounding errors. Always check `abs(pivot) < 1e-9` to treat near-zero as actual zero.

---

## Exercise 11 — Determinant

### Concept
A scalar that encodes whether a matrix is invertible and how much it scales volumes:

```
det(A) = (-1)^swaps × Π diagonals of the upper-triangular form
```

| det(A) | Meaning |
|---|---|
| ≠ 0 | matrix is invertible; it preserves dimensions |
| = 0 | matrix is singular; it collapses space (e.g. plane → line) |
| > 0 | transformation preserves orientation |
| < 0 | transformation flips orientation |

### Examples
```python
Matrix([[1., -1.], [-1., 1.]]).determinant()   # 0.0   (singular — rows are opposites)
Matrix([[2., 0.], [0., 2.]]).determinant()     # 4.0   (scales area by 4)
Matrix([[1., 0.], [0., 1.]]).determinant()     # 1.0   (identity — no change)

Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]]).determinant()
# -174.0

Matrix([[8., 5., -2., 4.], [4., 2.5, 20., 4.],
        [8., 5., 1., 4.], [28., -4., 17., 1.]]).determinant()
# 1032.0
```

### Shortcut via Row Echelon
1. Run `row_echelon()` on a copy, track swap count.
2. `det = product_of_diagonal × (-1)^swaps`

Each row swap flips the sign of the determinant.

---

## Exercise 12 — Inverse Matrix

### Concept
`A⁻¹` is the matrix that "undoes" `A`: `A · A⁻¹ = I`. Only exists when `det(A) ≠ 0`.

**Algorithm — Gauss-Jordan on [A | I]:**
1. Build augmented matrix `[A | I]` (append identity to the right).
2. Forward pass: reduce left half to upper-triangular form with partial pivoting, normalise each pivot row to 1.
3. Backward pass: eliminate entries *above* each pivot (full reduced row echelon).
4. Left half is now `I`; extract right half as `A⁻¹`.

### Examples
```python
Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).inverse()
# Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])   (identity is its own inverse)

Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]]).inverse()
# Matrix([[0.5, 0., 0.], [0., 0.5, 0.], [0., 0., 0.5]])

Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]]).inverse()
# Approximately:
# [[ 0.649…,  0.097…, -0.655…],
#  [-0.137…,  0.127…,  0.965…],
#  [-0.028…, -0.028…,  0.229…]]
```

### Sanity Check
`A × A⁻¹` should return the identity matrix (within floating-point tolerance `1e-9`).

---

## Exercise 13 — Rank

### Concept
The **rank** of a matrix is the number of **linearly independent rows** (equivalently, columns) — the true dimensionality of the space it spans.

```
rank(A) = number of non-zero rows in row echelon form
```

| Rank | Meaning |
|---|---|
| = min(rows, cols) | full rank — matrix spans its full space |
| < min(rows, cols) | rank-deficient — some rows/columns are redundant |

### Examples
```python
# Full rank 3×3 identity
Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).rank()   # 3

# Row 3 and Row 4 are duplicates → rank 2
Matrix([[1., 2., -1.], [2., 4., 2.], [0., 0., 1.], [0., 0., 1.]]).rank()  # 2

# 3×4 full row rank
Matrix([[8., 4., 7., 21.], [5., 7., 6., 18.], [-2., 20., 1., 7.]]).rank() # 3
```

### Relationship to Other Concepts
- `rank(A) = n` (full rank) ↔ `det(A) ≠ 0` ↔ `A⁻¹` exists (for square matrices).
- `rank(A) < n` ↔ the null space of `A` is non-trivial (there exist non-zero vectors `x` with `Ax = 0`).

---

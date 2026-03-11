import math

class Vector:
    def __init__(self, data): # 'data' should be a list of floats (K)
        """Store a list of floats as a vector and track its size."""
        self.data = [float(x) for x in data] #all your input values are converted to floats
        self.size = len(self.data)

    def add(self, v):
        """Add another vector component-wise and store the result in-place.
        Formula: w_i = u_i + v_i  for each i
        """
        if not isinstance(v, Vector):
            raise ValueError("Cannot add a scalar to a vector")
        if len(self.data) != len(v.data):
           raise ValueError("ValueError: Dimensions must match")
        for i in range(len(self.data)):
            self.data[i] += v.data[i]
        return self

    def sub(self, v):
        """Subtract another vector component-wise and store the result in-place.
        Formula: w_i = u_i - v_i  for each i
        """
        if not isinstance(v, Vector):
            raise ValueError("Cannot substract a scalar from a vector")
        if len(self.data) != len(v.data):
            raise ValueError("ValueError: Dimensions must match")
        for i in range(len(self.data)):
            self.data[i] -= v.data[i]
        return self

    def scl(self, a):
        """Scale the vector by scalar a in-place.
        Formula: w_i = a * u_i  for each i
        """
        for i in range(len(self.data)):
            self.data[i] *= a
        return self

    def dot(self, v):
        """Compute the dot (inner) product of two vectors.
        Formula: u · v = Σ u_i * v_i
        """
        if self.size != v.size:
            raise ValueError("Vectors should have the same size")
        result = 0.0
        for i in range(self.size):
            result += self.data[i] * v.data[i]
            #result = math.fma(self.data[i], v.data[i], result)
        return result

    def __str__(self):
        return f"Vector({self.data})"

    def norm_1(self):
        """Manhattan (L1) norm: sum of absolute values of components.
        Formula: ||u||_1 = Σ |u_i|
        """
        if self.size == 0:
            return 0.0
        return sum(abs(x) for x in self.data)

    def norm(self):
        """Euclidean (L2) norm: square root of the dot product with itself.
        Formula: ||u||_2 = sqrt(Σ u_i²) = sqrt(u · u)
        """
        if self.size == 0:
            return 0.0
        return pow(self.dot(self), 0.5)

    def norm_inf(self):
        """Supremum (L∞) norm: largest absolute value among all components.
        Formula: ||u||_∞ = max(|u_i|)
        """
        if self.size == 0:
            return 0.0
        return max(abs(x) for x in self.data)


class Matrix:
    def __init__(self, data): # 'data' is a list of lists [[row1], [row2]]
        """Store a 2D list of floats as a matrix and compute its shape (rows, cols)."""
        self.data = [[float(val) for val in row] for row in data]
        # Shape is (rows, columns)
        self.shape = (len(self.data), len(self.data[0])) if self.data else 0

    def add(self, m):
        """Add another matrix element-wise in-place (matrices must have the same shape).
        Formula: C_ij = A_ij + B_ij
        """
        if self.shape != m.shape:
            raise ValueError("ValueError: Dimensions must match")
        for i in range(len(self.data)):
            for k in range(len(self.data[i])):
                self.data[i][k] += m.data[i][k]
        return self

    def sub(self, m):
        """Subtract another matrix element-wise in-place (matrices must have the same shape).
        Formula: C_ij = A_ij - B_ij
        """
        if self.shape != m.shape:
            raise ValueError("ValueError: Dimensions must match")
        for i in range(len(self.data)):
            for k in range(len(self.data[i])):
                self.data[i][k] -= m.data[i][k]
        return self

    def scl(self, a):
        """Scale every element of the matrix by scalar a in-place.
        Formula: B_ij = a * A_ij
        """
        for i in range(len(self.data)):
            for k in range(len(self.data[i])):
                self.data[i][k] *= a
        return self

    def __str__(self):
        return f"Matrix({self.data})"

    def mul_vec(self, vec):
        """Multiply the matrix by a column vector (linear map).
        Formula: (Av)_i = Σ_j A_ij * v_j   (dot product of each row with vec)
        """
        if self.shape[1] != vec.size:
            raise ValueError("Matrix columns must match vector size")
        result_data = []
        for row in self.data:
            row_sum = 0.0
            for i in range(len(row)):
                #row_sum = math.fma(row[i], vec.data[i], row_sum)
                row_sum += row[i] * vec.data[i]
            result_data.append(row_sum)
        return Vector(result_data)

    def mul_mat(self, mat):
        """Multiply two matrices together (standard matrix product).
        Formula: C_ij = Σ_k A_ik * B_kj   (A must be m×n, B must be n×p → C is m×p)
        """
        if self.shape[1] != mat.shape[0]:
            raise ValueError("Matrix 1 columns must match Matrix 2 rows")

        new_matrix_data = []
        for i in range(self.shape[0]):
            new_row = []
            for j in range(mat.shape[1]):
                cell_sum = 0.0
                for k in range(self.shape[1]):
                    #cell_sum = math.fma(self.data[i][k], mat.data[k][j], cell_sum)
                    cell_sum += self.data[i][k] * mat.data[k][j]
                new_row.append(cell_sum)
            new_matrix_data.append(new_row)
        return Matrix(new_matrix_data)

    def trace(self):
        """Sum of the diagonal elements of a square matrix.
        Formula: tr(A) = Σ_i A_ii
        """
        if self.shape[0] != self.shape[1]:
            raise ValueError("Matrix should be square")
        result = 0.0
        for i in range(self.shape[0]):
            result += self.data[i][i]
        return result

    def transpose(self):
        """Flip the matrix over its main diagonal in-place: rows become columns.
        Formula: A^T_ij = A_ji
        """
        transposed_data = []
        for column in range(self.shape[1]):
            new_row = []
            for row in range(self.shape[0]):
                new_row.append(self.data[row][column])
            transposed_data.append(new_row)
        self.data = transposed_data
        self.shape = (len(self.data), len(self.data[0]))
        return self

    def row_echelon(self):
        """Reduce the matrix to row echelon form via Gaussian elimination with partial pivoting.
        Algorithm:
          For each column j, find the row with the largest absolute value (pivot),
          swap it to the current pivot row, then eliminate all entries below the pivot:
            factor = A_ij / A_pivot_j
            row_i -= factor * pivot_row
        Returns (reduced_matrix, swap_count) — swap_count is used by determinant().
        """
        rows, cols = self.shape
        pivot_row = 0
        swaps = 0
        for j in range(cols):
            if pivot_row >= rows:
                break
            max_row = pivot_row
            for i in range(pivot_row + 1, rows):
                if abs(self.data[i][j]) > abs(self.data[max_row][j]):
                    max_row = i
            if self.data[max_row][j] == 0:
                continue
            if max_row != pivot_row:
                self.data[pivot_row], self.data[max_row] = self.data[max_row], self.data[pivot_row]
                swaps += 1
            for i in range(pivot_row + 1, rows):
                factor = self.data[i][j] / self.data[pivot_row][j]
                for k in range(j, cols):
                    self.data[i][k] -= factor * self.data[pivot_row][k]
            pivot_row += 1
        return self, swaps

    def determinant(self):
        """Compute the determinant using row echelon form (Gaussian elimination).
        Algorithm:
          1. Reduce to upper triangular via row_echelon() and count row swaps.
          2. det = product of diagonal entries * (-1)^swaps
        Formula: det(A) = (-1)^swaps * Π_i U_ii   where U is the upper triangular form
        """
        if self.shape[0] != self.shape[1]:
            raise ValueError("Matrix must be square")
        temp_data = [row[:] for row in self.data]
        temp_matrix = Matrix(temp_data)
        triangular_matrix, swaps = temp_matrix.row_echelon()
        det = 1.0
        for i in range(self.shape[0]):
            det *= triangular_matrix.data[i][i]
        return det * ((-1) ** swaps)

    def inverse(self):
        """Compute the inverse via Gauss-Jordan elimination on the augmented matrix [A | I].
        Algorithm:
          1. Build augmented matrix [A | I].
          2. Forward elimination with partial pivoting to reach [U | L⁻¹].
          3. Back substitution to reach [I | A⁻¹].
          4. Extract the right half as A⁻¹.
        Formula: A * A⁻¹ = I
        """
        if self.determinant() == 0:
            raise ValueError("Matrix is singular and has no inverse")
        rows = self.shape[0]
        aug_data = []
        for i in range(rows):
            identity_row = [1.0 if j == i else 0.0 for j in range(rows)]
            aug_data.append(self.data[i] + identity_row)
        cols_aug = rows * 2
        for i in range(rows):
            max_r = i
            for k in range(i + 1, rows):
                if abs(aug_data[k][i]) > abs(aug_data[max_r][i]):
                    max_r = k
            aug_data[i], aug_data[max_r] = aug_data[max_r], aug_data[i]
            pivot_val = aug_data[i][i]
            for j in range(i, cols_aug):
                aug_data[i][j] /= pivot_val
            for k in range(i + 1, rows):
                factor = aug_data[k][i]
                for j in range(i, cols_aug):
                    aug_data[k][j] -= factor * aug_data[i][j]
        for i in range(rows - 1, -1, -1):
            for k in range(i - 1, -1, -1):
                factor = aug_data[k][i]
                for j in range(i, cols_aug):
                    aug_data[k][j] -= factor * aug_data[i][j]
        inv_data = [row[rows:] for row in aug_data]
        self.data = inv_data
        return self

    def rank(self):
        """Compute the rank: number of linearly independent rows (non-zero rows after reduction).
        Algorithm:
          1. Reduce to row echelon form via row_echelon().
          2. Count rows that contain at least one non-zero element (|x| > 1e-9).
        Formula: rank(A) = number of non-zero rows in row echelon form
        """
        temp_data = [row[:] for row in self.data]
        temp_matrix = Matrix(temp_data)
        triangular_matrix, _ = temp_matrix.row_echelon()
        rank_count = 0
        for row in triangular_matrix.data:
            is_zero_row = True
            for element in row:
                if abs(element) > 1e-9:
                    is_zero_row = False
                    break
            if not is_zero_row:
                rank_count += 1
        return rank_count

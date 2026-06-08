from vector_class import Vector

class Matrix:

    def __init__(self, data):
        """
        data : list of lists [[row1], [row2]]
        shape : (rows, cols)
        """
        self.data = []
        if isinstance(data, list):
            #Path 1: m1 = Matrix([[1.0, 2.0], [3.0, 4.0]]) - list of lists
            # loop validates numbers, ensures the grid is rectangular, and stores it.
            #all return true only if all elements True
            #elem = single row in matrix
            if all(isinstance(elem, list) and len(data[0]) == len(elem) and all(type(i) in [int, float, complex] for i in elem) for elem in data):
                self.data = data
                self.shape = (len(data), len(data[0])) 
		# a shape: Matrix((3, 3)) (the matrix will be filled with zeros by default)
        # Path 2: m2 = Matrix((3, 3)) - tuple representing dimensions.
        elif isinstance(data, tuple) and len(data) == 2 and all(isinstance(elem, int) and elem >= 0 for elem in data):
            for i in range(data[0]):
                row = []
                for j in range(data[1]):
                    row.append(0)
                self.data.append(row)
                self.shape = (data[0], data[1])
        else:
            raise ValueError("Invalid form of data,", data)


    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Invalid type of input value")
            #raise TypeError(f"Invalid input: {func.__name__} requires a Matrix object.")
        if self.shape != other.shape:
            raise ValueError(f"ValueError: Dimensions must match")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Matrix(result)


    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Invalid type of input value")
            #raise TypeError(f"Invalid input: {func.__name__} requires a Matrix object.")
        if self.shape != other.shape:
            raise ValueError(f"ValueError: Dimensions must match")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Matrix(result)


    def __mul__(self, other):
        if any(isinstance(other, scalar_type) for scalar_type in [int, float, complex]):
            result = [[self.data[i][j] * other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Matrix(result)
        
        elif isinstance(other, Vector):
            if self.shape[1] != other.shape[0]:
                raise ValueError("ValueError: Dimensions must match")
            result = [[sum([self.data[i][k] * other.data[k][j] for k in range(self.shape[1])]) for j in range(other.shape[1])] for i in range(self.shape[0])]
            return Vector(result)
        
        elif isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise ValueError("ValueError: Dimensions must match")
            result = [[sum([self.data[i][k] * other.data[k][j] for k in range(self.shape[1])]) for j in range(other.shape[1])] for i in range(self.shape[0])]
            return Matrix(result)
        else:
            raise TypeError("Invalid type of input value")
          

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

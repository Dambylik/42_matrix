from ex04_norm import Vector
import math

class Matrix:
    def __init__(self, data):
        self.data = [[float(val) for val in row] for row in data]
        self.shape = (len(self.data), len(self.data[0])) if self.data else 0

    def add (self, m):
        if self.shape != m.shape:
            raise ValueError("ValueError: Dimensions must match")
        for i in range(len(self.data)):
            for k in range(len(self.data[i])):
                self.data[i][k] += m.data[i][k]
        return self

    def sub(self, m):
        if self.shape != m.shape:
            raise ValueError("ValueError: Dimensions must match")
        for i in range(len(self.data)):
            for k in range(len(self.data[i])):
                self.data[i][k] -= m.data[i][k]
        return self

    def scl(self, a):
        for i in range(len(self.data)):
            for k in range(len(self.data[i])):
                self.data[i][k] *= a
        return self

    def __str__(self):
        return f"Matrix({self.data})"
    
    def mul_vec(self, vec):
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
        if self.shape[0] != self.shape[1]:
            raise ValueError("Matrix should be square")
        result = 0.0
        for i in range(self.shape[0]):
            result += self.data[i][i]
        return result
    
    def transpose(self):
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
        """det(A)=(−1)^swaps x diagonals"""
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
        # 1. Create a deep copy of the data
        temp_data = [row[:] for row in self.data]
        temp_matrix = Matrix(temp_data)
        
        # 2. Get the Row Echelon Form
        # We ignore 'swaps' because it doesn't affect the rank
        triangular_matrix, _ = temp_matrix.row_echelon()
        rank_count = 0
        
        # 3. Count rows that are not all zeros
        for row in triangular_matrix.data:
            is_zero_row = True
            for element in row:
                if abs(element) > 1e-9:
                    is_zero_row = False
                    break       
            if not is_zero_row:
                rank_count += 1            
        return rank_count


def main():
    u = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    print(u.rank())
    print("-" * 50) 

    u = Matrix([[1.0, 2.0, -1.0], [2.0, 4.0, 2.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]])
    print(u.rank())
    print("-" * 50)  

    u = Matrix([[8.0, 4.0, 7.0, 21.0], [5.0, 7.0, 6.0, 18.0], [-2.0, 20.0, 1.0, 7.0]])
    print(u.rank())
    print("-" * 50) 


if __name__ == '__main__':
    main()
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

    
def main():
    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    print(u.trace())
    print("-" * 50) 

    u = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
    print(u.trace())
    print("-" * 50)  

    u = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]])
    print(u.trace())
    print("-" * 50) 


if __name__ == '__main__':
    main()
from vector_class import Vector
import numpy as np


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


    def mul_vec(self, other):
        if isinstance(other, Vector):
            if self.shape[1] != other.size:
                raise ValueError("Matrix columns must match vector size")
            
            other.data = np.reshape(other.data, (self.shape[1], -1)).tolist()
            other.shape = (self.shape[1], 1)
            result = [[sum([self.data[i][k] * other.data[k][j] for k in range(self.shape[1])]) for j in range(other.shape[1])] for i in range(self.shape[0])]
            return Vector(result)
        else:
            raise TypeError("Invalid type of input value.")


    def mul_mat(self, other):
        if isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise  ValueError("Matrix 1 columns must match Matrix 2 rows")
            result = [[sum([self.data[i][k] * other.data[k][j] for k in range(self.shape[1])]) for j in range(other.shape[1])] for i in range(self.shape[0])]
            return Matrix(result)
        else:
            raise TypeError("Invalid type of input value.")


    def trace(self):
        if self.shape[0] != self.shape[1]:
            raise TypeError("Matrix should be square")
        trace = 0.0
        for i in range(self.shape[0]):
            trace += self.data[i][i]
        return trace
    

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
		# gaussian elimination with back-substitution for reduced row echelon from
        pivot = 0
        for row in range(self.shape[0]):
            if pivot >= self.shape[1]:
                break
			# find a non-zero pivot element in the current pivot
            while self.data[row][pivot] == 0:
                pivot += 1
                if pivot >= self.shape[1]:
                    return self
			# swap the current row with a row containing a non-zero pivot element
            for i in range(row + 1, self.shape[0]):
                if self.data[i][pivot] != 0:
                    self.data[row], self.data[i] = self.data[i], self.data[row]
                    break
			# scale the current row to make the pivot element 1
            divisor = self.data[row][pivot]
            self.data[row] = [elem / divisor for elem in self.data[row]]

			# perform the row operations to eliminate other non-zero elements in the current column
            for i in range(self.shape[0]):
                if i != row:
                    multiplier = self.data[i][pivot]
                    self.data[i] = [elem - multiplier * self.data[row][j] for j, elem in enumerate(self.data[i])]
            pivot += 1
        return self



    def determinant(self):
        if self.shape[0] != self.shape[1]:
            raise TypeError("Matrix must be square.")
	
		# base case for 2 x 2 matrix
        if self.shape[0] == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        matrix_copy = [row.copy() for row in self.data]
        det = 1.0
		
		# gaussian elimination
        for i in range(self.shape[0]):
			# find the pivot
            for j in range(i, self.shape[0]):
                if matrix_copy[j][i] != 0:
					# swap rows if necessary
                    if i != j:
                        matrix_copy[i], matrix_copy[j] = matrix_copy[j], matrix_copy[i]
                        det *= -1
					
					# scale the current row to make the pivot element 1
                    pivot = matrix_copy[i][i]
                    det *= pivot
                    matrix_copy[i] = [elem / pivot for elem in matrix_copy[i]]
					
					# eliminate other non-zero elements in the same column
                    for k in range(i + 1, self.shape[0]):
                        factor = matrix_copy[k][i]
                        matrix_copy[k] = [x - y * factor for x, y in zip(matrix_copy[k], matrix_copy[i])]
                    break
        return det


    def inverse(self):
        if self.shape[0] != self.shape[1]:
            raise TypeError("Inverse is undefined for non-square matrices.")
        if self.determinant() == 0:
            raise ValueError(f"Matrix is not invertable.")
        # create an augmented matrix [A|I]
        augmented_matrix = [row + [float(i == j) for j in range(self.shape[0])] for i, row in enumerate(self.data)]
        augmented_matrix = Matrix(augmented_matrix)

        # apply Gauss-Jordan elimination to obtain the reduced row-echelon form
        rref_matrix = augmented_matrix.row_echelon()

        # extract the inverse matrix [I|B]
        inverse_matrix = [row[self.shape[0]:] for row in rref_matrix.data]
        return inverse_matrix
    

    def rank(self):
        matrix_copy = Matrix(self.data)
        # apply Gauss-Jordan elimination to obtain the reduced row-echelon form
        matrix_copy.row_echelon()
        rank = 0
        # count the number of non-zero rows
        for row in matrix_copy.data:
            if any(row):
                rank += 1
        return rank

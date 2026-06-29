
class Matrix:

    def __init__(self, data):
        """
        data : list of lists [[row1], [row2]]
        shape : tunple (rows, cols)
        """
        self.data = []
        if isinstance(data, list):
            #if shape is list of lists: Matrix([[1.0, 2.0], [3.0, 4.0]])
            if all(isinstance(elem, list) and len(data[0]) == len(elem) and all(type(i) in [int, float] for i in elem) for elem in data):
                self.data = data
                self.shape = (len(data), len(data[0])) 
		# if shape is tuple: Matrix((3, 3)) (the matrix will be filled with zeros by default)
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
        if self.shape != other.shape:
            raise ValueError(f"ValueError: Dimensions must match")
        
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Matrix(result)


    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Invalid type of input value")
        if self.shape != other.shape:
            raise ValueError(f"ValueError: Dimensions must match")
        
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Matrix(result)


    def __mul__(self, other):
        from vector_class import Vector
        if any(isinstance(other, scalar_type) for scalar_type in [int, float]):
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
        from vector_class import Vector
        if not isinstance(other, Vector):
            raise TypeError("Invalid type of input value.")
            
        matrix_cols = len(self.data)
        matrix_rows = len(self.data)
        flat_v = [num for row in other.data for num in row]
        
        if matrix_cols != len(flat_v):
            raise ValueError("Matrix columns must match vector size")
            
        result = []
        for i in range(matrix_rows):
            row_sum = 0.0
            for j in range(matrix_cols):
                row_sum += self.data[i][j] * flat_v[j]
            result.append([row_sum])       
        return Vector(result)


    def mul_mat(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Invalid type of input value.")
            
        self_rows = len(self.data)
        self_cols = len(self.data)
        other_rows = len(other.data)
        other_cols = len(other.data)
        
        if self_cols != other_rows:
            raise ValueError("Matrix 1 columns must match Matrix 2 rows")
            
        result = []
        for i in range(self_rows):
            new_row = []
            for j in range(other_cols):
                dot_sum = 0.0
                for k in range(self_cols): 
                    dot_sum += self.data[i][k] * other.data[k][j]
                new_row.append(dot_sum)
            result.append(new_row)
        return Matrix(result)


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
        return Matrix(transposed_data)


    def row_echelon(self):
        pivot = 0
        for row in range(self.shape[0]):
            if pivot >= self.shape[1]:
                return self
            
            # find the first non-zero number (pivot) in the current column.
            search_row = row
            while self.data[search_row][pivot] == 0:
                search_row += 1
                if search_row == self.shape[0]:
                    search_row = row
                    pivot += 1
                    if pivot == self.shape[1]:
                        return self
                        
            # swap rows if necessary to bring that non-zero number to the current row.
            self.data[row], self.data[search_row] = self.data[search_row], self.data[row]
            
            # scale (divide) the entire row by the pivot to scale the pivot to 1.
            divisor = self.data[row][pivot]
            self.data[row] = [elem / divisor for elem in self.data[row]]

            # subtract scaled versions of this row from ALL other rows to force the rest of the column to 0.
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
		
		# find the first non-zero number (pivot) in the current column.
        for i in range(self.shape[0]):
            for j in range(i, self.shape[0]):
                if matrix_copy[j][i] != 0:
					# swap rows if necessary to bring that non-zero number to the current row.
                    if i != j:
                        matrix_copy[i], matrix_copy[j] = matrix_copy[j], matrix_copy[i]
                        det *= -1
					
					# scale (divide) the entire row by the pivot to scale the pivot to 1.
                    pivot = matrix_copy[i][i]
                    det *= pivot
                    matrix_copy[i] = [elem / pivot for elem in matrix_copy[i]]
					
					# subtract other non-zero elements in the same column
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
        n = self.shape[0]
        augmented_matrix = []

        for i, row in enumerate(self.data):
            identity_row = []
            for j in range(n):
                if i == j:
                    identity_row.append(1.0)
                else:
                    identity_row.append(0.0)
            new_row = row + identity_row
            augmented_matrix.append(new_row)
        augmented_matrix = Matrix(augmented_matrix)

        ref_matrix = augmented_matrix.row_echelon()
        
        # extract the inverse matrix A⁻¹
        inverse_matrix = [row[self.shape[0]:] for row in ref_matrix.data]
        return inverse_matrix
    

    def rank(self):
        matrix_copy = Matrix(self.data)
        matrix_copy.row_echelon()
        
        rank = 0
        # count the number of non-zero rows
        for row in matrix_copy.data:
            if any(row):
                rank += 1
        return rank


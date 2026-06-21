import math
import numpy as np

class Vector:

    def __init__(self, data): # 'data' should be a list of floats (K)
        '''
        Forcing to define the 2D geometry of the vector.
        They must type Vector([[1.0, 2.0, 3.0]]) (Row)
        They must type Vector([[1.0], [2.0], [3.0]]) (Column)
        '''
        self.data = []
        # when data is a list
        if isinstance(data, list): # if row vector([[0.0, 1.0, 2.0, 3.0]]) is a list of a list of floats
            if len(data) == 1 and isinstance(data[0], list) and len(data[0]) > 0 and all(type(i) in [int, float, complex] for i in data[0]):	
                self.data = data
                self.shape = (1, len(data[0])) #(1, N) = one row and N columns
                self.size = len(data[0])
                # if Vector([[0.0], [1.0], [2.0], [3.0]]) is a list of lists of single float
            elif all(isinstance(elem, list) and len(elem) == 1 and all(type(i) in [int, float, complex] for i in elem) for elem in data):
                self.data = data
                self.shape = (len(data), 1) #(N, 1) = N rows and one column
                self.size = len(data)
            else:
                raise ValueError("Invalid form of list,", data)
        else:
            raise ValueError("Invalid form of data,", data)


    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Cannot add a scalar to a vector")
        if self.shape != other.shape:
            raise ValueError("ValueError: Dimensions must match")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Vector(result)


    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Cannot substract a scalar from a vector")
        if self.shape != other.shape:
            raise ValueError("ValueError: Dimensions must match")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Vector(result)


    def __mul__(self, other):
        if any(isinstance(other, scalar_type) for scalar_type in [int, float, complex]):
            result = [[self.data[i][j] * other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Vector(result)
        
        elif isinstance(other, Vector):
            if self.shape[1] != other.shape[0]:
                raise ValueError("ValueError: Dimensions must match")
            result = [[self.data[i][j] * other for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Vector(result)
        
        else:
            from matrix_class import Matrix
            if isinstance(other, Matrix):
                if self.shape[1] != other.shape[0]:
                    raise ValueError("ValueError: Dimensions must match")
                result = [[sum([self.data[i][k] * other.data[k][j] for k in range(self.shape[1])]) for j in range(other.shape[1])] for i in range(self.shape[0])]
                return Matrix(result)
            raise TypeError("Invalid type of input value")


    @staticmethod
    #Normally, methods inside a class require self as their first parameter because they act upon a specific object's data (e.g., u.add(v) modifies u). You use it when a function logically relates to your class, but it processes external inputs rather than modifying a single, existing instance.
    def linear_combination(lst_vectors, coefs):
        if not all(isinstance(lst, list) for lst in [lst_vectors, coefs]):
            raise ValueError("Invalid form of list")
        
        if not all(isinstance(v, Vector) for v in lst_vectors):
            raise TypeError("Invalid input: list should contain only Vectors.", lst_vectors)
        
        if not all(v.size == lst_vectors[0].size for v in lst_vectors):
            raise TypeError("Invalid input: list of Vectors should contain Vectors of the same shape.", lst_vectors)
        
        if len(coefs) != len(lst_vectors) or not all(type(i) in [int, float] for i in coefs):
            raise TypeError("Size of vector and scalar should be identical")

        v_shape = lst_vectors[0].shape
        v = Vector([[0.0] * v_shape[1] for _ in range(v_shape[0])]) #build a 2D grid: for Row Vector (1, 3) and for Column Vector (3, 1)
        for vector, coef in zip(lst_vectors, coefs):
            for i in range(v.shape[0]):
                for j in range(v.shape[1]):
                    v.data[i][j] = math.fma(vector.data[i][j], coef, v.data[i][j])
        return (v)


    @staticmethod
    def lerp(u, v, t):
        if type(u) != type(v):
            raise TypeError("Invalid input: uncompatiable type")
        
        if not (isinstance(t, float) and (0 <= t <= 1)):
            raise ValueError("Invalid value: a real number from 0 to 1 required.", t)
        
        if isinstance(u, (int, float, complex)):
                return math.fma(v - u, t, u) # Apply fma directly to flat numbers
        else:
            result = type(u)([[0.0] * u.shape[1] for _ in range(u.shape[0])])
            for i in range(u.shape[0]):
                for j in range(u.shape[1]):
                    result.data[i][j] = math.fma(v.data[i][j] - u.data[i][j], t, u.data[i][j])
            return result



    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Invalid input: uncompatiable type")
        if self.size != other.size:
            raise ValueError("Vectors should have the same size")
        
        # 1. Flatten both 2D data grids into simple 1D sequences
        flat_self = []
        for row in self.data:
            for num in row:
                flat_self.append(num)
                
        flat_other = []
        for row in other.data:
            for num in row:
                flat_other.append(num)
        
        result = 0.0

        # 2. Loop through the flat sequences using a single index
        for i in range(self.size):
            result = math.fma(flat_self[i], flat_other[i], result)  
        return result


    def norm_1(self):
        abs_sum = 0.0
        lst_data = np.reshape(self.data, (1, -1))[0]
        for elem in lst_data:
            if elem >= 0:
                abs_sum += elem
            else:
                abs_sum -= elem
        return abs_sum


    def norm(self):
        squared_sum = 0.0
        lst_data = np.reshape(self.data, (1, -1))[0]
        for elem in lst_data:
            squared_sum += elem ** 2
        return squared_sum ** 0.5


    def norm_inf(self):
        max_abs_value = float('-inf')
        lst_data = np.reshape(self.data, (1, -1))[0]
        for elem in lst_data:
            if elem >= 0:
                abs_value = elem
            else:
                abs_value = -elem
            if abs_value > max_abs_value:
                max_abs_value = abs_value
        return max_abs_value


    def angle_cos(u: Vector, v: Vector) -> float:
        if not all(isinstance(vec, Vector) for vec in [u, v]):
            raise TypeError("Vectors should have the same size")
        if u.size != v.size:
            raise TypeError("Vectors should have the same size")
        
        cosine_similarity = u.dot(v) / (u.norm() * v.norm())
        return np.around(cosine_similarity, decimals=10)


    @staticmethod
    def cross_product(u: Vector, v: Vector) -> Vector:
        if not (u.size == 3 and u.size == v.size):
            raise ValueError("Vector should have 3 dimensions")
        
        # Flattening the 2D data and unpacking it into three variables in one step
        x1, y1, z1 = [num for row in u.data for num in row]
        x2, y2, z2 = [num for row in v.data for num in row]

        cross_x = (y1 * z2 - y2 * z1)
        cross_y = (z1 * x2 - z2 * x1)
        cross_z = (x1 * y2 - x2 * y1)
        
        return Vector([[cross_x, cross_y, cross_z]])

    def __str__(self):
        return f"Vector({self.data})"

    

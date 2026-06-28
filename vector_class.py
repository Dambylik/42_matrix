import math


class Vector():

    def __init__(self, data):
        '''
        Forcing to define the 2D geometry of the vector.
        They must type Vector([[1.0, 2.0, 3.0]]) (Row)
        They must type Vector([[1.0], [2.0], [3.0]]) (Column)
        '''
        self.data = []
        # when data is a list
        if isinstance(data, list): # if vector is a list of a list of floats ([[0.0, 1.0, 2.0, 3.0]]) 
            if len(data) == 1 and isinstance(data[0], list) and len(data[0]) > 0 and all(type(i) in [int, float] for i in data[0]):	
                self.data = data
                self.shape = (1, len(data[0])) #(1, N) = one row and N columns
                self.size = len(data[0])
                # if vector is a list of lists of single float ([[0.0], [1.0], [2.0], [3.0]]) 
            elif all(isinstance(elem, list) and len(elem) == 1 and all(type(i) in [int, float] for i in elem) for elem in data):
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
        if any(isinstance(other, scalar_type) for scalar_type in [int, float]):
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
    def linear_combination(lst_vectors, scalar):
        if not all(isinstance(lst, list) for lst in [lst_vectors, scalar]):
            raise ValueError("Size of vector and scalar should be identical")
        
        if not all(isinstance(v, Vector) for v in lst_vectors):
            raise TypeError("Invalid input: list should contain only Vectors.", lst_vectors)
        
        if not all(v.size == lst_vectors[0].size for v in lst_vectors):
            raise TypeError("Invalid input: list of Vectors should contain Vectors of the same shape.", lst_vectors)
        
        if len(scalar) != len(lst_vectors) or not all(type(i) in [int, float] for i in scalar):
            raise TypeError("Size of vector and scalar should be identical")

        result_size = lst_vectors[0].size
        result = Vector([[0.0] * result_size])
        for vector, coef in zip(lst_vectors, scalar):
            result += vector * coef
        return (result)


    @staticmethod
    def lerp(u, v, t):
        from matrix_class import Matrix

        if type(u) != type(v):
            raise TypeError("Invalid input: uncompatiable type")
        
        if not (isinstance(t, float) and (0 <= t <= 1)):
            raise ValueError("Invalid value: a real number from 0 to 1 required.", t)
        
        if any(isinstance(u, accepted_type) for accepted_type in [int, float, Vector, Matrix]):
            return u + (v - u) * t 
        else:
            raise TypeError("Invalid input: unsupported type")


    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Invalid input: incompatible type")
        if self.size != other.size:
            raise ValueError("Vectors should have the same size")
        
        # Flatten both vectors into 1D lists
        flat_self = [elem for row in self.data for elem in row]
        flat_other = [elem for row in other.data for elem in row]
        
        result = 0.0
        for i in range(self.size):
            result += flat_self[i] * flat_other[i]           
        return result


    def norm_1(self):
        abs_sum = 0.0
        for row in self.data:
            for elem in row:
                if elem >= 0:
                    abs_sum += elem
                else:
                    abs_sum -= elem
        return abs_sum


    def norm(self):
        squared_sum = 0.0
        for row in self.data:
            for elem in row:
                squared_sum += elem ** 2            
        return squared_sum ** 0.5


    def norm_inf(self):
        max_abs_value = 0.0       
        for row in self.data:
            for elem in row:
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
        return round(cosine_similarity, 10)


    @staticmethod
    def cross_product(u: Vector, v: Vector) -> Vector:
        if not (u.size == 3 and u.size == v.size):
            raise ValueError("Vector should have 3 dimensions")
        
        # Flatten both vectors into 1D lists
        x1, y1, z1 = [num for row in u.data for num in row]
        x2, y2, z2 = [num for row in v.data for num in row]

        cross_x = (y1 * z2 - y2 * z1)
        cross_y = (z1 * x2 - z2 * x1)
        cross_z = (x1 * y2 - x2 * y1)        
        return Vector([[cross_x, cross_y, cross_z]])


    def __str__(self):
        return f"Vector({self.data})"

    

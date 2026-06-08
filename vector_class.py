import math


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

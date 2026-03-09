import math

class Vector:
    def __init__(self, data): # 'data' should be a list of floats (K)
        self.data = [float(x) for x in data] #all your input values are converted to floats
        self.size = len(self.data)

    def add(self, v):
        if not isinstance(v, Vector):
            raise ValueError("Cannot add a scalar to a vector")
        if len(self.data) != len(v.data):
           raise ValueError("ValueError: Dimensions must match")
        for i in range(len(self.data)):
            self.data[i] += v.data[i]
        return self

    def sub(self, v):
        if not isinstance(v, Vector):
            raise ValueError("Cannot substract a scalar from a vector")
        if len(self.data) != len(v.data):
            raise ValueError("ValueError: Dimensions must match")
        for i in range(len(self.data)):
            self.data[i] -= v.data[i]
        return self

    def scl(self, a):
        for i in range(len(self.data)):
            self.data[i] *= a 
        return self
    
    def dot (self, v):
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
        """Manhattan Norm : L^1 = ||u||_1 = ∑ |u_i|"""
        if self.size == 0:
            return 0.0
        return sum(abs(x) for x in self.data)

    def norm(self):
        """Euclidean Norm :L^2 =  ||u||_2 = sqrt∑(u_i)^2"""
        if self.size == 0:
            return 0.0
        return pow(self.dot(self), 0.5)

    def norm_inf(self):
        """Supreme Norm : L^∞ = ||u||_∞ = max(|u_i|)"""
        if self.size == 0:
            return 0.0
        return max(abs(x) for x in self.data)


def main():
    u = Vector([0.0, 0.0])
    print(u.norm_1(), u.norm(), u.norm_inf())
    print("-" * 50)

    u = Vector([1.0, 2.0, 3.0])
    print(u.norm_1(), u.norm(), u.norm_inf())   
    
    print("-" * 50) 
    u = Vector([-1.0, -2.0])
    print(u.norm_1(), u.norm(), u.norm_inf());


if __name__ == '__main__':
    main()

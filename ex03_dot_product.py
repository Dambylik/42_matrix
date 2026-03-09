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


def main():
    u = Vector([0.0, 0.0])
    v = Vector([1.0, 1.0])
    print(u.dot(v))
    print("-" * 50)
    
    u = Vector([1.0, 1.0])
    v = Vector([1.0, 1.0])
    print(u.dot(v))
    print("-" * 50)

    u = Vector([-1.0, 6.0])
    v = Vector([3.0, 2.0])
    print(u.dot(v))


if __name__ == '__main__':
    main()

class Vector:
    def __init__(self, data): # 'data' should be a list of floats (K)
        self.data = [float(x) for x in data] #all your input values are converted to floats
        self.size = len(self.data)

    def add(self, v) :
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

    def __str__(self):
        return f"Vector({self.data})"


class Matrix:
    def __init__(self, data): # 'data' is a list of lists [[row1], [row2]]
        self.data = [[float(val) for val in row] for row in data]
        # Shape is (rows, columns)
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
    

def main():
    v_1 = Vector([2.0, 3.0])
    v_2 = Vector([5.0, 7.0])

    m_1 = Matrix([[1.0, 2.0],
                  [3.0, 4.0]])
    m_2 = Matrix([[7.0, 4.0],
                  [-2.0, 2.0]])
    a = 2.0
    
    print ("Added vector :", v_1.add(v_2))
    #print ("Substracted vector :", v_1.sub(v_2))
    #print ("Scaled vector :", v_1.scl(a))
    print ("-" * 50)
    #print ("Added matrix :", m_1.add(m_2))
    #print ("Substracted matrix :", m_1.sub(m_2))
    #print ("Scaled matrix :", m_1.scl(a))
    return


if __name__ == '__main__':
    main()




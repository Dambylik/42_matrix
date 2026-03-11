from linear_algebra import Vector, Matrix

def main():
    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Vector([4.0, 2.0])
    print(u.mul_vec(v))
    print("-" * 50) 

    u = Matrix([[2.0, 0.0], [0.0, 2.0]])
    v = Vector([4.0, 2.0])
    print(u.mul_vec(v))
    print("-" * 50)  

    u = Matrix([[2.0, -2.0], [-2.0, 2.0]])
    v = Vector([4.0, 2.0])
    print(u.mul_vec(v))
    print("-" * 50)  

    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Matrix([[1.0, 0.0], [0.0, 1.0]])
    print(u.mul_mat(v))
    print("-" * 50) 

    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Matrix([[2.0, 1.0],[4.0, 2.0]])
    print(u.mul_mat(v))
    print("-" * 50) 

    u = Matrix([[3.0, -5.0], [6.0, 8.0]])
    v = Matrix([[2.0, 1.0], [4.0, 2.0]])
    print(u.mul_mat(v))
    print("-" * 50) 

if __name__ == '__main__':
    main()
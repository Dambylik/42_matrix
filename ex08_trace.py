from linear_algebra import Vector, Matrix

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
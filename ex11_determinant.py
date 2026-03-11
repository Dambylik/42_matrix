from linear_algebra import Vector, Matrix

def main():
    u = Matrix([[1.0, -1.0], [-1.0, 1.0]])
    print(u.determinant())
    print("-" * 50) 

    u = Matrix([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
    print(u.determinant())
    print("-" * 50)  

    u = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
    print(u.determinant())
    print("-" * 50) 

    u = Matrix([[8.0, 5.0, -2.0, 4.0], [4.0, 2.5, 20.0, 4.0], [8.0, 5.0, 1.0, 4.0], [28.0, -4.0, 17.0, 1.0] ])
    print(u.determinant())
    print("-" * 50) 

if __name__ == '__main__':
    main()
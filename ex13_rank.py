from linear_algebra import Vector, Matrix

def main():
    u = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    print(u.rank())
    print("-" * 50) 

    u = Matrix([[1.0, 2.0, -1.0], [2.0, 4.0, 2.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]])
    print(u.rank())
    print("-" * 50)  

    u = Matrix([[8.0, 4.0, 7.0, 21.0], [5.0, 7.0, 6.0, 18.0], [-2.0, 20.0, 1.0, 7.0]])
    print(u.rank())
    print("-" * 50) 


if __name__ == '__main__':
    main()
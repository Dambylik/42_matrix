from linear_algebra import Vector, Matrix


def main():
    u = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    result, swaps = u.row_echelon()
    print(result)
    print(f"Swaps: {swaps}")
    print("-" * 50) 

    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    result, swaps = u.row_echelon()
    print(result)
    print(f"Swaps: {swaps}")
    print("-" * 50) 

    u = Matrix([[1.0, 2.0], [2.0, 4.0]])
    result, swaps = u.row_echelon()
    print(result)
    print(f"Swaps: {swaps}")
    print("-" * 50) 

    u = Matrix([[8.0, 5.0, -2.0, 4.0, 28.0], [4.0, 2.5, 20.0, 4.0, -4.0], [8.0, 5.0, 1.0, 4.0, 17.0]])
    result, swaps = u.row_echelon()
    print(result)
    print(f"Swaps: {swaps}")
    print("-" * 50) 

if __name__ == '__main__':
    main()
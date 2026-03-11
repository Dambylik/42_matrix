from linear_algebra import Vector, Matrix

def main():
    u = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    print(f"Original: {u} has a shape {u.shape}" )
    print(f"Transposed: {u.transpose()} has a shape {u.shape}")
    print("shape: ", u.shape)
    print("-" * 50) 

    u = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
    print(f"Original: {u} has a shape {u.shape}" )
    print(f"Transposed: {u.transpose()} has a shape {u.shape}")
    print("-" * 50)  

    u = Matrix([[-2.0, -8.0, 4.0]])
    print(f"Original: {u} has a shape {u.shape}" )
    print(f"Transposed: {u.transpose()} has a shape {u.shape}")
    print("-" * 50) 


if __name__ == '__main__':
    main()
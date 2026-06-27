"""
Add, Subtract a two vectors/matrices of the same size; 
Multiply a vector/matrix by a scalar

Time complexity : O(n) - time scales linearly with the data size (n)
Space complexity : O(n) - builds a new copy of the data (size n).
"""

from matrix_class import Matrix
from vector_class import Vector


def main():
    u = Vector([[2., 3.]])
    v = Vector([[5., 7.]])
    
    print("\nAddition:", u + v) # [7.0][10.0]
    print ("Substraction:", u - v) # [-3.0][-4.0]
    print ("Scaled:", u * 2) # [4.0][6.0]

    print ("-" * 50)

    u = Matrix([[1., 2.], [3., 4.]])
    v = Matrix([[7., 4.], [-2., 2.]])
    
    print ("\nAddition:", u + v) # [8.0, 6.0][1.0, 6.0]
    print ("Substraction:", u - v) # [-6.0, -2.0][5.0, 2.0]
    print ("Scaled:", u * 2) # [2.0, 4.0][6.0, 8.0]
    
    return


if __name__ == '__main__':
    main()




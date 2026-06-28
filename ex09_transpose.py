"""
Computes the transpose of a given matrix.
Flip the matrix over its main diagonal so that the original rows become the new columns.

Formula: A_T(ij) = A(ji)

Time complexity: O(nm) - visit and move every single number in the matrix only once.
Space complexity: O(nm) - because the dimensions change we must build a new matrix in memory to store the flipped data.
"""

from matrix_class import Matrix


def main():
    m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
    print("original:", m1)
    print("transposed:", m1.transpose()) # [[0., 2., 4.], [1., 3., 5.]]
    print("-" * 50) 
    
    m1 = Matrix([[0., 2., 4.], [1., 3., 5.]])
    print("original:", m1)
    print("transposed:", m1.transpose()) # [[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]]
    print("-" * 50) 


if __name__ == '__main__':
    main()
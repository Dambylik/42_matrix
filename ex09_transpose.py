"""
Computes the transpose matrix of a given matrix.
Flip the matrix over its main diagonal in-place: rows become columns.
Formula: A^T_ij = A_ji

Time complexity : O(nm)
Space complexity : O(nm)
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
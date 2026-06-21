"""
Compute the determinant of the given matrix using row echelon form (Gaussian elimination).
Algorithm:
    1. Reduce to upper triangular via row_echelon() and count row swaps.
    2. det = product of diagonal entries * (-1)^swaps
Formula: det(A) = (-1)^swaps * Π_i U_ii   where U is the upper triangular form

Time complexity : O(n^3)
Space complexity : O(n^3)
"""

from matrix_class import Matrix


def main():
    u = Matrix([[ 1., -1.],[-1., 1.]]);
    print(u.determinant()); # 0.0
    print("-" * 50)

    u = Matrix([[2., 0., 0.],[0., 2., 0.],[0., 0., 2.]]);
    print(u.determinant()); # 8.0
    print("-" * 50)

    u = Matrix([[8., 5., -2.],[4., 7., 20.],[7., 6., 1.]]);
    print(u.determinant()); # -174.0
    print("-" * 50)

    u = Matrix([[ 8., 5., -2., 4.],[ 4., 2.5, 20., 4.],[ 8., 5., 1., 4.],[28., -4., 17., 1.]]);
    print(u.determinant()); # 1032
    print("-" * 50) 
     

if __name__ == '__main__':
    main()
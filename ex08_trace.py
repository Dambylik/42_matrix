"""
Computes the trace of the given matrix.
Sum of the diagonal elements of a square matrix.
Formula: tr(A) = sum of main diagonal

Time complexity : O(n)
"""

from matrix_class import Matrix


def main():
    u = Matrix([[1., 0.],[0., 1.]])
    print(u.trace()); # 2.0
    print("-" * 50) 

    u = Matrix([[2., -5., 0.],[4., 3., 7.],[-2., 3., 4.]])
    print(u.trace()); # 9.0
    print("-" * 50) 

    u = Matrix([[-2., -8., 4.],[1., -23., 4.],[0., 6., 4.]])
    print(u.trace()); # -21.0
    print("-" * 50) 


if __name__ == '__main__':
    main()
"""
Compute the rank: number of linearly independent rows (non-zero rows after reduction).
Algorithm:
    1. Reduce to row echelon form via row_echelon().
    2. Count rows that contain at least one non-zero element (|x| > 1e-9).
Formula: rank(A) = number of non-zero rows in row echelon form

Time complexity : O(n^3) - requires nested looping through rows and columns.
"""
from matrix_class import Matrix

def main():
    u = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])
    print(u.rank()) # 3
    print("-" * 50) 

    u = Matrix([[ 1., 2., 0., 0.],[ 2., 4., 0., 0.],[-1., 2., 1., 1.]])
    print(u.rank()) # 2
    print("-" * 50) 

    u = Matrix([[ 8., 5., -2.],[ 4., 7., 20.],[ 7., 6., 1.],[21., 18., 7.]])
    print(u.rank()) # 3
    print("-" * 50) 


if __name__ == '__main__':
    main()
"""
Compute the row-echelon form of the given matrix.
Reduce the matrix to row echelon form via Gaussian elimination with partial pivoting.
Algorithm:
    For each column j, find the row with the largest absolute value (pivot),
    swap it to the current pivot row, then eliminate all entries below the pivot:
    factor = A_ij / A_pivot_j
    row_i -= factor * pivot_row
    Returns (reduced_matrix, swap_count) — swap_count is used by determinant().

Time complexity : O(n^3)
Space complexity : O(n^3)
"""

from matrix_class import Matrix


def main():
    u = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])
    print(u.row_echelon()); # [1.0, 0.0, 0.0][0.0, 1.0, 0.0][0.0, 0.0, 1.0]
    print("-" * 50) 

    u = Matrix([[1., 2.],[3., 4.]])
    print(u.row_echelon()); # [1.0, 0.0][0.0, 1.0]
    print("-" * 50) 

    u = Matrix([[1., 2.],[2., 4.]])
    print(u.row_echelon()); # [1.0, 2.0][0.0, 0.0]
    print("-" * 50) 

    u = Matrix([[8., 5., -2., 4., 28.],[4., 2.5, 20., 4., -4.],[8., 5., 1., 4., 17.]])
    print(u.row_echelon()); # [1.0, 0.625, 0.0, 0.0, -12.16][0.0, 0.0, 1.0, 0.0, -3.6][0.0, 0.0, 0.0, 1.0, 29.5 ]
    print("-" * 50) 



if __name__ == '__main__':
    main()
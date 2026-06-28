"""
Compute the row-echelon form of the given matrix.
Uses Gaussian elimination to transform the matrix. Every pivot 
(leading number in a row) becomes exactly 1. Every other number in that 
pivot's column becomes exactly 0.

Algorithm:
1. Find the first non-zero number (pivot) in the current column.
2. Swap rows if necessary to bring that non-zero number to the current row.
3. Divide the entire row by the pivot to scale the pivot to 1.
4. Subtract scaled versions of this row from ALL other rows to force the rest of the column to 0.

Time complexity : O(n^3) - requires nested looping through rows and columns.
Space complexity : O(1) - modifies the original list in-place.
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
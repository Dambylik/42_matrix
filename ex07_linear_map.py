"""
Multiply a matrix by a vector or a matrix by a matrix.

Multiply the matrix by a column vector (linear map).
Formula: vec = dot product of (matrix_row x vector)

Multiply two matrices together (standard matrix product).
Formula: U = sum of (row x column) 

Time complexity: 
- mul_vec: O(mn) to compute the dot product of m rows with an n-length vector.
- mul_mat: O(mnp) to compute all nested dot products between the two matrices.

Space complexity: 
- mul_vec: O(m) to store the resulting column vector.
- mul_mat: O(mp) to store the newly created m x p matrix.
"""

from matrix_class import Matrix
from vector_class import Vector


def main():
    u = Matrix([[1., 0.], [0., 1.]])
    v = Vector([[4., 2.]])
    print(u.mul_vec(v)); # [4.][2.]
    print("-" * 50) 

    u = Matrix([[2., 0.],[0., 2.]])
    v = Vector([[4., 2.]])
    print(u.mul_vec(v)); # [8.][4.]
    print("-" * 50) 

    u = Matrix([[2., -2.],[-2., 2.]])
    v = Vector([[4., 2.]])
    print(u.mul_vec(v)); # [4.][-4.]
    print("-" * 50) 

    u = Matrix([[1., 0.],[0., 1.]])
    v = Matrix([[1., 0.],[0., 1.]])
    print(u.mul_mat(v)); # [1., 0.][0., 1.]
    print("-" * 50) 

    u = Matrix([[1., 0.],[0., 1.]])
    v = Matrix([[2., 1.],[4., 2.]])
    print(u.mul_mat(v)); # [2., 1.][4., 2.]
    print("-" * 50) 

    u = Matrix([[3., -5.],[6., 8.]])
    v = Matrix([[2., 1.],[4., 2.]])
    print(u.mul_mat(v)); # [-14., -7.][44., 22.]
    print("-" * 50) 


if __name__ == '__main__':
    main()
"""
Multiply a matrix by a vector or a matrix by a matrix.

Multiply the matrix by a column vector (linear map).
Formula: (Av)_i = Σ_j A_ij * v_j   (dot product of each row with vec)

Multiply two matrices together (standard matrix product).
Formula: C_ij = Σ_k A_ik * B_kj   (A must be m x n , B must be n x p -> C is m x p)

Time complexity : O(nm)
Space complexity : O(nm)
The complexity of these functions is O(nmp), where n, m, and p are the dimensions of the input matrices and vectors.
The mul_vec function has a complexity of O(n*m) because it loops for each row of the self matrix (n loops) and for each column of the other vector (m loops) to perform the corresponding dot product.
The mul_mat function has a complexity of O(nmp) because it loops for each row of the self matrix (n loops) and for each column of the other matrix (p loops) and for each column of the self matrix and 
for each row of the other matrix (m loops) to perform the corresponding dot product.
The space complexity of the mul_mat function is O(n*p), where n is the number of rows of the self matrix and p is the number of columns of the other matrix.
"""

from matrix_class import Vector, Matrix


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
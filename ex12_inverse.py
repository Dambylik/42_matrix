"""
Compute the inverse via Gauss-Jordan elimination on the augmented matrix [A | I].
Algorithm:
    1. Build augmented matrix [A | I].
    2. Forward elimination with partial pivoting to reach [U | L⁻¹].
    3. Back substitution to reach [I | A⁻¹].
    4. Extract the right half as A⁻¹.
Formula: A * A⁻¹ = I

Time complexity : O(n^3)
Space complexity : O(n^3)
"""

from matrix_class import Matrix


def main():
    u = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])
    print(u.inverse())# [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]
    print("-" * 50) 

    u = Matrix([[2., 0., 0.],[0., 2., 0.],[0., 0., 2.]])
    print(u.inverse())# [0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]
    print("-" * 50) 

    u = Matrix([[8., 5., -2.],[4., 7., 20.],[7., 6., 1.]])
    print(u.inverse())# [0.649425287, 0.097701149, -0.655172414],[-0.781609195, -0.126436782, 0.965517241], [0.143678161, 0.074712644, -0.206896552]
    print("-" * 50) 


if __name__ == '__main__':
    main()
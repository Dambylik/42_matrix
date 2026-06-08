"""
Add, Subtract a two vectors/matrices of the same size; 
Multiply a vector/matrix by a scalar

Time complexity : O(n) - time scales linearly with the data size (n)
Space complexity : O(n) - builds a new copy of the data (size n).
"""

from matrix_class import Matrix
from vector_class import Vector


def main():
    u = Vector([[2., 3.]])
    v = Vector([[5., 7.]])
    a = 2.
    print("\nAddition:", u + v)
    print ("Substraction:", u - v)
    print ("Scaled:", u * a)

    print ("-" * 50)

    m_1 = Matrix([[1., 2.], [3., 4.]])
    m_2 = Matrix([[7., 4.], [-2., 2.]])
    b = 2.
    print ("\nAddition:", m_1 + m_2)
    print ("Substraction:", m_1 - m_2)
    print ("Scaled:", m_1 * b)
    return


if __name__ == '__main__':
    main()




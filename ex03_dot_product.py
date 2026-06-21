"""
Compute dot product of two vectors of the same
dimension.
Formula: u · v = Σ u_i * v_i

Time complexity : O(n) - time scales linearly with the data size (n)
Space complexity : O(n) - builds a new copy of the data (size n).
"""

from vector_class import Vector


def main():
    u = Vector([[0., 0.]])
    v = Vector([[1.], [1.]]);
    print(u.dot(v)) # 0.0
    print("-" * 50)
    
    u = Vector([[1., 1.]])
    v = Vector([[1.], [1.]])
    print(u.dot(v)) # 2.0
    print("-" * 50)

    u = Vector([[-1., 6.]])
    v = Vector([[3.], [2.]])
    print(u.dot(v)) # 9.0


if __name__ == '__main__':
    main()

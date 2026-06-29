"""
Compute the cosine of the angle between two vectors using the dot product.
Formula: cos(θ) = (u * v) / (||l2_u|| * ||l2_v||)

Time complexity : O(n) - time scales linearly with the data size (n)
Space complexity : O(n) - builds a new copy of the data (size n).
"""

from vector_class import Vector


def main():
    u = Vector([[1., 0.]])
    v = Vector([[1., 0.]])
    print(Vector.angle_cos(u, v))
    print("-" * 50) # 1.0

    u = Vector([[1., 0.]])
    v = Vector([[0., 1.]])
    print(Vector.angle_cos(u, v))
    print("-" * 50) # 0.0

    u = Vector([[-1., 1.]])
    v = Vector([[ 1., -1.]])
    print(Vector.angle_cos(u, v))
    print("-" * 50)  # -1.0

    u = Vector([[2., 1.]])
    v = Vector([[4., 2.]])
    print(Vector.angle_cos(u, v))
    print("-" * 50) # 1.0

    u = Vector([[1., 2., 3.]])
    v = Vector([[4., 5., 6.]])
    print(Vector.angle_cos(u, v)) # 0.974631846
    print("-" * 50) 


if __name__ == '__main__':
    main()

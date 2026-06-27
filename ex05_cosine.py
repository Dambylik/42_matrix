"""
Compute the cosine of the angle between two vectors using the dot product.
Formula: cos(θ) = (u * v) / (||l2||_u * ||l2||_v)

The complexity of this function depends on the dot and norm methods which are both O(n), where n is the size of the vectors.
Therefore, the total complexity of angle_cos is also O(n).
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

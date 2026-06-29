"""
Compute the cross product of two 3D vectors, returning a vector orthogonal to both.
Formula: w = (u_y * v_z - u_z * v_y,  u_z * v_x - u_x * v_z,  u_x * v_y - u_y * v_x)
"""

from vector_class import Vector


def main():
    u = Vector([[0., 0., 1.]])
    v = Vector([[1., 0., 0.]])
    print(Vector.cross_product(u, v)) # [0.][1.][0.]
    print("-" * 50) 

    u = Vector([[1., 2., 3.]])
    v = Vector([[4., 5., 6.]])
    print(Vector.cross_product(u, v)) # [-3.][6.][-3.]
    print("-" * 50) 

    u = Vector([[4., 2., -3.]]);
    v = Vector([[-2., -5., 16.]]);
    print(Vector.cross_product(u, v)); # [17.][-58.][-16.]
    print("-" * 50)


if __name__ == '__main__':
    main()
"""
Compute different kinds of norms.
- L1-norm (Manhattan norm): sum of absolute values of components.
Formula: ||l1|| = sum(|u_i|)

- L2-norm (Euclidean norm): square root of the dot product with itself.
Formula: ||l2|| = sqrt(sum(u_i)²)

- L∞-norm (Supremum norm): - largest absolute value among all components.
Formula: ||L∞|| = max(|u_i|)

Time complexity : O(n) - time scales linearly with the data size (n)
Space complexity : O(n) - builds a new copy of the data (size n).
"""

from vector_class import Vector


def main():
    u = Vector([[0., 0., 0.]])
    print(u.norm_1(), u.norm(), u.norm_inf()) # 0.0, 0.0, 0.0
    print("-" * 50)

    u = Vector([[1., 2., 3.]])
    print(u.norm_1(), u.norm(), u.norm_inf()) # 6.0, 3.7416573867739413, 3.0   
    
    print("-" * 50) 
    u = Vector([[-1., -2.]])
    print(u.norm_1(), u.norm(), u.norm_inf()) # 3.0, 2.23606797749979, 2.0


if __name__ == '__main__':
    main()

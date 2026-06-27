"""
Linear interpolation between two values at position t ∈ [0, 1].
Formula: lerp(u, v, t) = u + (v - u) * t 
When you write lerp(21.0, 42.0, 0.3), you are asking the computer: "If I start at 21, and my destination is 42, exactly where am I when I have completed 30% of the journey?"

Time complexity : O(n) - time scales linearly with the data size (n)
Space complexity : O(n) - builds a new copy of the data (size n).
"""

from vector_class import Vector
from matrix_class import Matrix


def main ():
    print(Vector.lerp(0., 1., 0.)); # 0.0
    print(Vector.lerp(0., 1., 1.)); # 1.0
    print(Vector.lerp(0., 1., 0.5)); # 0.5
    print(Vector.lerp(21., 42., 0.3)); # 27.3
    print(Vector.lerp(Vector([[2., 1.]]), Vector([[4., 2.]]), 0.3)); #[2.6], [1.3]
    print(Vector.lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5)); # [[11., 5.5][16.5, 22.]]
    return


if __name__ == '__main__':
    main()
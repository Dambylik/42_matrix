"""
Compute a linear combination: scale each vector by its coefficient and sum them.
Formula: result = Σ coefs_i * u_i

Time complexity : O(n)
Space complexity : O(n)
"""

from vector_class import Vector


def linear_combination(u: list[Vector], coefs: list[float]) -> Vector:
   
    if len(u) != len(coefs):
        raise ValueError("Size of vector and scalar should be identical")
        
    if not u:
        raise ValueError("Vector should not be empty")

    dim = u[0].size
    result = [0.0] * dim

    for i in range(dim):
        for vector, scalar in zip(u, coefs):
            result[i] = (vector.data[i] * scalar) + result[i]
            #result[i] = math.fma(vector.data[i], scalar, result[i])

    return Vector(result)


def main():
	e1 = Vector([[1., 0., 0.]]);
	e2 = Vector([[0., 1., 0.]]);
	e3 = Vector([[0., 0., 1.]]);
	v1 = Vector([[1., 2., 3.]]);
	v2 = Vector([[0., 10., -100.]]);
	print(Vector.linear_combination([e1, e2, e3], [10., -2., 0.5])); # [10.][-2.][0.5]
	print(Vector.linear_combination([v1, v2], [10., -2.])); # [10.][0.][230.]



if __name__ == '__main__':
    main()

from ex00_add_subtract_scale import Vector
import math

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
    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([0.0, 10.0, -100.0])

    print(linear_combination([e1, e2, e3], [10.0, -2.0, 0.5]))
    print(linear_combination([v1, v2], [10.0, -2.0]))
    return


if __name__ == '__main__':
    main()

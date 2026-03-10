from ex04_norm import Vector

def angle_cos(u: Vector, v: Vector) -> float:
    """cos(θ)= (u * v) / ||u||_2 x ||v||_2"""
    if u.size != v.size:
        raise ValueError("Vectors should have the same size")
    normed_u = u.norm()
    normed_v = v.norm()
    if normed_u == 0.0 or normed_v == 0.0:
        return 0.0
    return u.dot(v) / (normed_u * normed_v) 


def main():
    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print(angle_cos(u, v))
    print("-" * 50) 

    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print(angle_cos(u, v))
    print("-" * 50) 

    u = Vector([-1., 1.])
    v = Vector([ 1., -1.])
    print(angle_cos(u, v))
    print("-" * 50) 

    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print(angle_cos(u, v))
    print("-" * 50) 

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(angle_cos(u, v))
    print("-" * 50) 


if __name__ == '__main__':
    main()

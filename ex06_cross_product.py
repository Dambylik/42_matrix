from ex04_norm import Vector

def cross_product(u: Vector, v: Vector) -> Vector:
    if u.size != 3 or v.size != 3:
        raise ValueError("Vector should have 3 dimensions")
    
    w_x = (u.data[1] * v.data[2]) - (u.data[2] * v.data[1])
    w_y = (u.data[2] * v.data[0]) - (u.data[0] * v.data[2])
    w_z = (u.data[0] * v.data[1]) - (u.data[1] * v.data[0])
    return Vector([w_x, w_y, w_z])


def main():
    u = Vector([0.0, 0.0, 1.0])
    v = Vector([1.0, 0.0, 0.0])
    print(cross_product(u, v))
    print("-" * 50) 

    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    print(cross_product(u, v))
    print("-" * 50) 

    u = Vector([4.0, 2.0, -3.0])
    v = Vector([-2.0, -5.0, 16.0])
    print(cross_product(u, v))
    print("-" * 50)


if __name__ == '__main__':
    main()
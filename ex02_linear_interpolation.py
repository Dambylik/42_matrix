from ex00_add_subtract_scale import Vector, Matrix
import math

def lerp(u: float, v: float, t: float) -> Vector:
    """ f(u,v,t) = u + t(v-u)
        f(u,v,t) = (1-t)u + tv
    """
    # Case 1: Scalars (floats/ints)
    if isinstance(u, (int, float)) and isinstance(v, (int, float)):
        #return math.fma(t, (v - u), u)
        return (u + t*(v - u))

    # Case 2: Vectors
    if isinstance(u, Vector) and isinstance(v, Vector):
        if u.size != v.size:
            raise ValueError("Vectors should have the same size")
                      
        result_vector = []
        for i in range(u.size):
            #val = math.fma(t, (v.data[i] - u.data[i]), u.data[i])
            val = u.data[i] + t*(v.data[i] - u.data[i])
            result_vector.append(val)
        return Vector(result_vector)

    # Case 3: Matrices
    if isinstance(u, Matrix) and isinstance(v, Matrix):
        if u.shape != v.shape:
            raise ValueError("Matrix should have the same dimensions")

        result_matrix = []
        for i in range(len(u.data)):
            row = []
            for j in range(len(u.data[i])):
                #val = math.fma(t, (v.data[i][j] - u.data[i][j]), u.data[i][j])
                val = (u.data[i][j] + t*(v.data[i][j] - u.data[i][j]))
                row.append(val)
            result_matrix.append(row)
        return Matrix(result_matrix)
    
    raise TypeError("Unsupported types for lerp")

def main ():
    print(lerp(0.0, 1.0, 0.0))
    print(lerp(0.0, 1.0, 1.0))
    print(lerp(0.0, 1.0, 0.5))
    print(lerp(21.0, 42.0, 0.3))
    print(lerp(Vector([2.0, 1.0]), Vector([4.0, 2.0]), 0.3))
    print(lerp(Matrix([[2.0, 1.0], [3.0, 4.0]]), Matrix([[20.0, 10.0], [30.0, 40.0]]), 0.5))
    return

if __name__ == '__main__':
    main()
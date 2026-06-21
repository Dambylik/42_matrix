import numpy as np
from matrix_class import Matrix
from vector_class import Vector


def complex_ex00():
    print("\nex00 vector complex number examples.\n")
    u = Vector([[2j, 3.]])
    v = Vector([[5j, 7.]])
    print("addition:\n", u + v) # [7j][10.0]
    print("subtraction:\n", u - v) # [-3j][-4.0]
    print("scalar multiplication:\n", u * 2j) # [-4+0j][6j]

    print("\nex00 matrix complex number examples.\n")
    u = Matrix([[1., 2j], [3., 4j]])
    v = Matrix([[7., 4j], [-2., 2j]])
    print("addition:\n", u + v) # [8.0, 6j][1.0, 6j]
    print("subtraction:\n", u - v) # [-6.0, -2j][5.0, 2j]
    print("scalar multiplication:\n", u * 2j) # [2j, -4+0j][6j, -8+0j]


def complex_ex01():
    print("\nex01 complex number examples.\n")
    v1 = Vector([[-42j, 42j]]);
    v2 = Vector([[-42j]]);
    v3 = Vector([[1., 3j]]);
    v4 = Vector([[10j, 20.]]);
    v5 = Vector([[3 - 42j, 100 + 1j, -69.5]]);
    v6 = Vector([[1j, 3j, 5j]]);

    print(Vector.linear_combination([v1], [-1.])); # '[42j, -42j]'
    print(Vector.linear_combination([v2, v2, v2], [-1., 1., 0.])); # '[0j]'
    print(Vector.linear_combination([v1, v3, v4], [1., -10., -1.])); # '[-10-52j, -20+12j]'
    print(Vector.linear_combination([v5, v6], [1., -10.])); # [3-52j, 100-29j, -69.5-50j]
    

def complex_ex02():
    print("\nex02 complex number examples.\n")
    print(Vector.lerp(-1 + 0j, 1 + 1j, 0.)); # -1+0j
    print(Vector.lerp(-1 + 0j, 1 + 1j, 1.)); # 1+1j
    print(Vector.lerp(2.2 + 0j, 3.5 + 42j, 0.5)); # 2.85+21j
    print(Vector.lerp(-42j, 42j, 0.5)); # 0j
    print(Vector.lerp(0j, 1j, 0.5)); # 0.5j
    print(Vector.lerp(21j, 42j, 0.3)); # 27.3j
    print(Vector.lerp(Vector([[-42j], [42j]]), Vector([[42j], [-42j]]), 0.5)); # [0j][0j]
    print(Vector.lerp(Vector([[4 - 2j], [-2 + 1j]]), Vector([[4 - 4j], [1 + 2j]]), 0.3)); # [4-2.6j][-1.1+1.3j]
    print(Vector.lerp(Matrix([[2j, 1j], [3j, 4j]]), Matrix([[20j, 10j], [30j, 40j]]), 0.5)); # [[11j, 5.5j][16.5j, 22j]]
    print("-" * 50)


def complex_ex03():
	print("\nex03 complex number examples.\n")
	u = Vector([[0j, 0j]]);
	v = Vector([[0j], [0j]]);
	print(u.dot(v)); # 0j

	u = Vector([[1j, 0j]]);
	v = Vector([[0j], [0j]]);
	print(u.dot(v)); # 0j

	u = Vector([[1j, 0j]]);
	v = Vector([[1j], [0j]]);
	print(u.dot(v)); # -1+0j

	u = Vector([[1j, 0j]]);
	v = Vector([[0j], [2j]]);
	print(u.dot(v)); # 0j

	u = Vector([[1j, 1j]]);
	v = Vector([[1j], [1j]]);
	print(u.dot(v)); # -2+0j

	u = Vector([[4j, 2j]]);
	v = Vector([[2j], [1j]]);
	print(u.dot(v)); # -10+0j
    print("-" * 50)


def complex_ex04():
	print("\nex04 complex number examples.\n")

	u = Vector([[1j, 2j, 3j]]);
	print(u.norm_1(), u.norm(), u.norm_inf());

	u = Vector([[-1., -2j]]);
	print(u.norm_1(), u.norm(), u.norm_inf());


def complex_ex05():
	print("\nex05 complex number examples.\n")
	v = Vector([[1j, 0.]]);
	u = Vector([[1j, 0.]]);
	print(Vector.angle_cos(u, v)); # 1+0j

	u = Vector([[1j, 0.]]);
	v = Vector([[0., 1j]]);
	print(Vector.angle_cos(u, v)); # -0-0j


def complex_ex06():
	print("\nex06 complex number examples.\n")
	u = Vector([[0j, 0., 1.]]);
	v = Vector([[1j, 0., 0.]]);
	print(Vector.cross_product(u, v)); # [0j][1j][0j]

	u = Vector([[1j, 2j, 3.]]);
	v = Vector([[4j, 5j, 6.]]);
	print(Vector.cross_product(u, v)); # [-3j][6j][3+0j]


def complex_ex07():
	print("\nex07 complex number examples.\n")
	u = Matrix([[2j, -2.],[-2., 2j]]);
	v = Vector([[4., 2.]]);
	print(u.mul_vec(v)); # [-4+8j][-8+4j]

	u = Matrix([[1., 0j],[0j, 1.]]);
	v = Matrix([[1., 0j],[0j, 1.]]);
	print(u.mul_mat(v)); # [1+0j, 0j][0j, 1+0j]


def complex_ex08():
	print("\nex08 complex number examples.\n")
	u = Matrix([[1j, 0.],[0., 1j]]);
	print(u.trace()); # 2j


def complex_ex09():
	print("\nex09 complex number examples.\n")
	u = Matrix([[1j, 2j],[3j, 4j]])
	print("transposed:", u.T()) # '[[1j, 3j], [2j, 4j]]'

def complex_ex10():
	print("\nex10 complex number examples.\n")
	u = Matrix([[1j, 2j],[3j, 4j]]);
	print(u.row_echelon()); # [1+0j, 0j][0j, 1+0j]


def complex_ex11():
	print("\nex11 complex number examples.\n")
	u = Matrix([[ 1j, 0.],[0., 1j]]);
	print(u.determinant()); # -1+0j


def complex_ex12():
	print("\nex12 complex number examples.\n")
	u = Matrix([[1j, 0., 0.],[0., 1j, 0.],[0., 0., 1j]]);
	print(u.inverse())# [-1j, 0j, 0j][0j, -1j, 0j][0j, 0j, -1j]


def complex_ex13():
	print("\nex13 complex number examples.\n")
	u = Matrix([[1j, 0., 0.],[0., 1j, 0.],[0., 0., 1j]])
	print(u.rank()) # 3


if __name__ == "__main__":
    complex_ex00()
    complex_ex01()
    complex_ex02()
    complex_ex03()
    complex_ex04()
    complex_ex05()
    complex_ex06()
    complex_ex07()
    complex_ex08()
    complex_ex09()
    complex_ex10()
    complex_ex11()
    complex_ex12()
    complex_ex13()
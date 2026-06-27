"""
Compute a linear combination: scale each vector by its coefficient and sum them.
Formula: result = sum (v * scalar)

Time complexity : O(n) - time scales linearly with the data size (n)
Space complexity : O(n) - builds a new copy of the data (size n).
"""

from vector_class import Vector


def main():
	e1 = Vector([[1., 0., 0.]])
	e2 = Vector([[0., 1., 0.]])
	e3 = Vector([[0., 0., 1.]])
 
	v1 = Vector([[1., 2., 3.]])
	v2 = Vector([[0., 10., -100.]])
 
	print(Vector.linear_combination([e1, e2, e3], [10., -2., 0.5])) # [10.][-2.][0.5]
	print(Vector.linear_combination([v1, v2], [10., -2.])) # [10.][0.][230.]



if __name__ == '__main__':
    main()

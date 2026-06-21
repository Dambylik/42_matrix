"""
Computes a projection matrix to be used to render 3D objects.
Formula : s = PVMp
s = position of the point on screen
P = projection matrix
V = view matrix
M = model matrix
p = position of the point in the 3D space

View matrix V is defined as:
V = RT
T = translation matrix
R = rotation matrix
"""

import math

def	projection(fov, ratio, near, far):
	projection_matrix = [[0.0] * 4 for _ in range(4)]

	projection_matrix[0][0] = 1 / (ratio * math.tan(fov / 2))
	projection_matrix[1][1] = -1 / (math.tan(fov / 2))
	projection_matrix[2][2] = (far) / (far - near) 
	projection_matrix[2][3] = (2 * far * near) / (far - near) 
	projection_matrix[3][2] = 1

	return projection_matrix


if __name__ == "__main__":
	# field of view in degrees
	fov = 100.0
	# window size ratio (width / height)
	ratio = 3 / 2
	# distance of the near plane
	near = 2.0
	# distance of the far plane
	far = 50.0
	projection_matrix = projection(fov, ratio, near, far)
	lst = '\n'.join(','.join(str(elem) for elem in row) for row in projection_matrix)
	
	print(lst)
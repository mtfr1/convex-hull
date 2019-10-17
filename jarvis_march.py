#return < 0 if c is on the left, > 0 if c is on the right, 0 if collinear
def cross_product(a, b, c):
	y1 = a[1] - b[1]
	y2 = a[1] - c[1]
	x1 = a[0] - b[0]
	x2 = a[0] - c[0]
	return y2*x1 - y1*x2

def distance(a, b, c):
	y1 = a[1] - b[1]
	y2 = a[1] - c[1]
	x1 = a[0] - b[0]
	x2 = a[0] - c[0]

	i1 = (y1**2 + x1**2)
	i2 = (y2**2 + y2**2)

	if(i1 == i2):
		return 0
	elif(i1 < i2):
		return -1
	return 1

def leftmost_point(S):
	point = S[0]
	for i in range(len(S)):
		if S[i][0] < point[0]:
			point = S[i]
	return point

#S is a set of points
def jarvis(points):
	starting_point = leftmost_point(points)
	result = set() #contains every point from the convex hull
	collinear_points = []
	result.add(starting_point)

	current = starting_point
	while True:
		next_point = points[0]

		for i in range(1, len(points)):
			if points[i] == current:
				continue
			pos = cross_product(current, next_point, points[i])

			if pos > 0:
				next_point = points[i]
				collinear_points.clear()
			
			elif pos == 0:
				if(distance(current, next_point, points[i]) < 0):
					collinear_points.append(next_point)
					next_point = points[i]
				else:
					collinear_points.append(points[i])
		for i in range(len(collinear_points)):
			result.add(collinear_points[i])
		if next_point == starting_point:
			break
		result.add(next_point)
		current = next_point

	return result
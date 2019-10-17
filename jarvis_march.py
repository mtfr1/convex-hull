#return < 0 if c is on the left, > 0 if c is on the right, 0 if collinear
def cross_product(o, a, b):
	return (b[1] - o[1]) * (a[0] - o[0]) - (a[1] - o[1]) * (b[0] - o[0])

def distance(a, b, c):
	i1 = ((a[1] - b[1])**2 + (a[0] - b[0])**2)
	i2 = ((a[1] - c[1])**2 + (a[0] - c[0])**2)

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
	return point, i

#S is a set of points
def jarvis(points):
	starting_point, aux = leftmost_point(points)
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

points = [(-7,8),(-4,6),(2,6),(6,4),(8,6),(7,-2),(4,-6),(8,-7),(0,0),(3,-2),(6,-10),(0,-6),
		(-9,-5),(-8,-2),(-8,0),(-10,3),(-2,2),(-10,4)]

print(jarvis(points))
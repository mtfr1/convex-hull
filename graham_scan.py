#return < 0 if c is on the left, > 0 if c is on the right, 0 if collinear
def cross_product(o, a, b):
	return (b[1] - o[1]) * (a[0] - o[0]) - (a[1] - o[1]) * (b[0] - o[0])

#implementation of Monotone Chain
#to avoid sorting by polar angle
def graham(points):
	points = list(set(points)) #remove duplicates

	if len(points) <= 2:
		return points
	
	points = sorted(points)

	L = [] #lower convex hull
	
	for point in points: #[0, n[
		while(len(L) >= 2) and (cross_product(L[-2], L[-1], point) <= 0):
			L.pop() 
		L.append(point)
	
	U = [] #upper convex hull
	
	for point in reversed(points): #]n, 0]
		while(len(U) >= 2) and (cross_product(U[-2], U[-1], point) <= 0):
			U.pop()
		U.append(point)

	return L[:-1] + U[:-1] #last point is the same as starting point
#return < 0 if c is on the left, > 0 if c is on the right, 0 if collinear
def cross_product(o, a, b):
	return (b[1] - o[1]) * (a[0] - o[0]) - (a[1] - o[1]) * (b[0] - o[0])

def leftmost_point(S):
	point = S[0]
	for i in range(len(S)):
		if S[i][0] < point[0]:
			point = S[i]
	return point, i

#S is a set of points
def jarvis(points):
    points = list(set(points))
    n = len(points)
    
    if(n <= 2):
        return points
    
    result = []
    
    starting_point, index = leftmost_point(points) #returns the index and the leftmost point
    point_on_hull = starting_point
    
    while True:
        result.append(point_on_hull)
        
        endpoint = points[0]
        
        for j in range(1, n):
            if endpoint == point_on_hull or cross_product(point_on_hull, points[j], endpoint) < 0:
                endpoint = points[j]
        
        point_on_hull = endpoint
        
        if endpoint == starting_point: #looped through the array
            break
            
    return result
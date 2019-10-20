#return < 0 if c is on the left, > 0 if c is on the right, 0 if collinear
def cross_product(o, a, b):
    return (b[1] - o[1]) * (a[0] - o[0]) - (a[1] - o[1]) * (b[0] - o[0])

def polar_sort(points, p0):
    return sorted(points, key=lambda p1:  math.atan2(p1[1]-p0[1], p1[0]-p0[0]))

def graham(points):
    points = list(set(points))
    
    stack = []
    P0, index = leftmost_point(points)
    points[0], points[index] = points[index], points[0]
    
    n_iter = 0
    ans = {}

    s_points = polar_sort(points[1:], points[0])
    
    stack.append(points[0])
    ans[n_iter] = hv.Path(stack)
    n_iter += 1
    
    stack.append(s_points[0])
    ans[n_iter] = hv.Path(stack)
    n_iter += 1
    
    for i in range(2, len(s_points)):
        while len(stack) >= 2 and cross_product(stack[-2], stack[-1], s_points[i]) <= 0:
            stack.pop()
            ans[n_iter] = hv.Path(stack)
            n_iter += 1
        
        stack.append(s_points[i])
        ans[n_iter] = hv.Path(stack)
        n_iter += 1
    
    ans[n_iter] = hv.Path(stack + [points[0]])
    return stack, ans
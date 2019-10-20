def orientation(p0, p1, p2):
    a = (p1[0] - p0[0], p1[1] - p0[1])
    b = (p2[0] - p0[0], p2[1] - p0[1])
    return a[0]*b[1] - b[0]*a[1]
    
def incremental(points):
    points = list(set(points))
    points = sorted(points)
    
    prox = {}
    prev = {}
    CH = []

    prox[0] = 1
    prev[0] = 1
    prox[1] = 0
    prev[1] = 0
    
    CH.append(points[0])
    CH.append(points[1])
    
    for i in range(2, len(points)):
        CH.append(points[i])
      
        if points[i][1] > points[i-1][1]:
            prox[i] = i - 1
            prev[i] = prev[i-1]
        
        else:
            prev[i] = i-1
            prox[i] = prox[i-1]
        
        prox[prev[i]] = i
        prev[prox[i]] = i
        
        prox_1 = prox[i]
        prox_2 = prox[prox[i]]
        
        while orientation(points[i], points[prox_1], points[prox_2]) > 0:
            prox[i] = prox_2
            prev[prox_2] = i
            
            CH = [p for p in CH if p != points[prox_1]]
            
            aux = sort_polar(CH, CH[getMinIndex(CH)])
            ans[n_iter] = hv.Path(aux+[aux[0]])
            n_iter += 1
            
            prox_1 = prox_2
            prox_2 = prox[prox_1]
            
        prev_1 = prev[i]
        prev_2 = prev[prev[i]]
        
        while orientation(points[i], points[prev_2], points[prev_1]) > 0:
            prev[i] = prev_2
            prox[prev_2] = i
    
            CH = [p for p in CH if p != points[prev_1]]
            
            prev_1 = prev_2
            prev_2 = prev[prev_1]
            
    return CH
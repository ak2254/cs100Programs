'''import point
origin = point.Point(0, 0)
pointA = point.Point(3,6)
print(origin.distanceTo(pointA))

pointB = point.Point(0,6)
pointC = point.Point(4,7)
pointD = point.Point(7,8)
k = ((origin.distanceTo(pointB) + origin.distanceTo(pointC) + origin.distanceTo(pointD))/3)
print(k)'''

lst = []
distance = 0
while len(lst) <= 100:
    import random
    point = point.Point(random.randint(0,100),random.randint(0,100))
    k = lst.append(point)
    for points in lst:
        if origin.distanceTo(points) < distance:
            distance = origin.distanceTo(points)
        else:
            continue
    return distance

    

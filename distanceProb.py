
lst = []
distance = 0
while len(lst) <= 100:
    import random
    import point 
    point = point.Point(random.randint(0,100),random.randint(0,100))
    k = lst.append(point)
    origin = point.Point(0,0)
    for points in lst:
        if origin.distanceTo(points) < distance:
            distance = origin.distanceTo(points)
        else:
            continue
print(distance)

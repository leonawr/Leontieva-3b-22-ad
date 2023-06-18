points = [(1, 2), (3, 4), (-1, 5), (6, -3)]


def distance(point):
    a, b = point[0], point[1]
    return (a ** 2 + b ** 2) ** 0.5

sorted_points = sorted(points, key=distance)

print(sorted_points)
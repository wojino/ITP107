n = int(input('How many points to read? '))

points = []
for i in range(n):
    x = float(input('x: '))
    y = float(input('y: '))
    points.append((x,y))

def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

distances = []
for i in range(n):
    distances.append(distance(points[i], points[(i+1)%n]))

def perimeter(distances):
    return sum(distances)

def longest_segment(distances):
    return max(distances)

print('Perimeter: %.1f' % perimeter(distances))
print('Longest segment length: %.1f' % longest_segment(distances))
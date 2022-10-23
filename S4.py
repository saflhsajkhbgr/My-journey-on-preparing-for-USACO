inp = input().split()
N = int(inp[0])
C = int(inp[1])
halfC = C/2
points = set([])
points = [int(i) for i in input().split()]
pointset = set(points)
counter = 0

# axis = [i+1 for i in range(C)]
ans = 0
for p1 in range(len(points)):
    for p2 in range(p1+1, len(points)):
        if abs(points[p1]-points[p2]) != halfC and points[p1]!=points[p2]:
            p1alter = int(min(points[p1]+halfC, points[p2]+halfC))
            p2alter = int(max(points[p1]+halfC, points[p2]+halfC))
            if p1alter < C and p2alter < C:
                p3 = [int(i) for i in range(p1alter+1, p2alter)]
            if p1alter >= C and p2alter >= C:
                p3 = [int(i) for i in range(p1alter-C+1, p2alter-C)]
            if p1alter < C and p2alter >= C:
                p3 = [int(i) for i in range(p2alter-C+1, p1alter)]
            print(points[p1], points[p2], p3)
            for p in p3:
                if p in pointset:
                    print(points[p1], points[p2], p)
                    counter += 1

print(counter)
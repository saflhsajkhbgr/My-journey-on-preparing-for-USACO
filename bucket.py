_ = float('inf')

with open('buckets.in', 'r') as file:
    grid = []
    while True:
        line = file.readline().split()
        if not line:
            break
        grid.append(line)
        if 'L' in line:


_ = float('inf')

with open('traffic.in', 'r') as file:
    N = file.readline()
    roads = []
    for i in range(int(N)):
        line = file.readline().split()
        roads.append(line)


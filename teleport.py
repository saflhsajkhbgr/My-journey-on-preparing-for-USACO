
with open('teleport.in', 'r') as file:
    line = file.readline().split()
    start = int(line[0])
    end = int(line[1])
    x = int(line[2])
    y = int(line[3])

direct_distance = abs(end-start)

start_to_x = abs(start-x)
y_to_end = abs(end-y)
d1 = start_to_x + y_to_end

start_to_y = abs(start-y)
x_to_end = abs(end-x)
d2 = start_to_y + x_to_end

ans = min(direct_distance, d1, d2)
with open('teleport.out', 'w') as file:
    file.write(str(ans))

n = int(input())
line = [int(i) for i in input().split()]
distance = 0
for i in range(n):
    m = 0
    for j in range(i+1, n):
        if line[j] > m:
            m = line[j]
        if j - i == 1:
            # print(i+1, j+1)
            distance += 2
        if line[j] <= line[i]:
            if line[j+1] > m:
                distance += j+2-i
                # print(i+1, j+2)
        else:
            break

print(distance)

# n = int(input())
ans = 0
change = []
days = []
# for i in range(n):
#     line = input().split()
#     change.append(line)
#     days.append(int(line[0]))
print(change)
print(days)
with open('measurement.in', 'r') as file:
    n = int(file.readline())
    for i in range(n):
        line = file.readline().split()
        change.append(line)
        days.append(int(line[0]))

# Elsie, Bessie, Mildred
_ = float('inf')
cows = [7, 7, 7]
while days != [_ for i in range(len(days))]:
    mini = min(days)
    # print(mini)
    minindex = days.index(mini)
    # print(minindex)
    days[minindex] = _
    day = change[minindex]

    m1 = max(cows)
    m1pos = cows.index(m1)
    c1 = cows.count(m1)
    # print(day)
    # print(day[1])
    if day[1] == 'Elsie':
        cows[0] += int(day[2])
    if day[1] == 'Bessie':
        cows[1] += int(day[2])
    if day[1] == 'Mildred':
        cows[2] += int(day[2])

    m2 = max(cows)
    m2pos = cows.index(m2)
    c2 = cows.count(m2)
    # print(cows)

    if not (m1pos == m2pos and c1 == c2):
        # print('activated')
        ans += 1
    # print('')
# print(ans)
with open('measurement.out', 'w') as file:
    file.write(str(ans))

n = int(input())

anss = []
for i in range(n):
    num = int(input())
    line = input().split()
    periods = []
    for k in line:
        periods.append(int(k))
    total = sum(periods)

    if len(set(periods)) == 1:
        print(0)
        continue

    multiplyers = []
    for j in range(1, total+1):
        if total % j == 0:
            multiplyers.append(j)

    for factor in multiplyers:
        ans = 0
        x = 0
        flag = False
        for k in range(len(periods)):
            x += periods[k]
            ans += 1
            if x == factor:
                x = 0
                ans = ans - 1
            if x > factor:
                flag = True
                break
        if flag:
            continue
        else:
            break
    print(ans)
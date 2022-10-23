
n = int(input())

anss = []
for i in range(n):
    num = int(input())
    classes = [int(i) for i in input().split()]
    total = sum(classes)

    if len(set(classes)) == 1:
        print(0)
        continue

    factors = []
    for j in range(1, total+1):
        if total % j == 0:
            factors.append(j)

    for factor in factors:
        ans = 0
        s = 0
        flag = False
        for k in range(num):
            s += classes[k]
            ans += 1
            if s == factor:
                s = 0
                ans -= 1
            if s > factor:
                flag = True
                break
        if flag:
            continue
        else:
            break
    print(ans)


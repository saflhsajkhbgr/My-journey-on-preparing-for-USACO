

n = int(input())
current = [int(i) for i in input().split()]
target = [int(i) for i in input().split()]

indices = {}

for i, j in enumerate(target):
    indices[j] = i

# ans = 0
# for i in range(n):
#     ind = target.index(current[-(i+1)])
#     for j in range(i, n):
#         if ind < indices[current[-(j+1)]]:
#             ans += 1
#             break

ans = 0
for i in range(n):
    # ind = target.index(current[-(i+1)])
    for j in range(i, n):
        if target[j] != current[-(i+1)]:
            pass
        else:
            ans += 1
            break
        # if ind < indices[current[-(j+1)]]:
        #     ans += 1
        #     break

print(ans)
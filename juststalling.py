
N = input()
cows = [int(i) for i in input().split()]
homes = [int(i) for i in input().split()]

# cows = [1, 2, 3, 4]
# homes = [2, 4, 3, 4]

c = 0
ans = 1
while len(cows) > 1:
    tallest = max(cows)
    indices = [i for i in range(len(homes)) if homes[i] >= tallest]
    # print(indices)
    A = len(indices)-c
    # print(A)
    ans = ans * A
    c += 1
    cows.remove(tallest)

print(ans)
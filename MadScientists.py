

with open('breedflip.in') as f:
    n = f.readline()
    A = f.readline()
    B = f.readline()


ans = 0
for i in range(int(n)):
    if A[i] != B[i]:
        if A[i-1] != B[i-1]:
            pass
        else:
            ans += 1

print(ans)

with open('breedflip.out', 'w') as file:
    file.write(str(ans))
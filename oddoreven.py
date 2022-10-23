
n = int(input())
odd = 0
even = 0
"""
6 odds 2 evens
4 odds 3 evens
"""
inp = [int(i) for i in input().split()]
for i in inp:
    if i%2 == 0:
        even += 1
    else:
        odd += 1

while odd > even:
    odd -= 2
    even += 1
if even > odd +1:
    even = odd + 1
print(even+odd)

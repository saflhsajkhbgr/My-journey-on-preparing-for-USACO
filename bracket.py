from collections import deque
inp = input()
stack = deque()
ans = True
for sub in inp:
    if sub == '(' or sub == '[':
        stack.append(sub)
    if sub == ')':
        top = stack.pop()
        if top != '(':
            ans = False
            break
    if sub == ']':
        top = stack.pop()
        if top != '[':
            ans = False
            break
if stack:
    ans = False
print(ans)

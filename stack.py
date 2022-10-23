
string = input()

from collections import deque
stack = deque()

stack.append(string[0])
for i in string[1:]:
    top = stack.pop()
    temp = []
    if i == top:
        stack.append(i)
    if top == '(':
        if i == ']':
            break
        elif i == ')':
            temp.append(')')
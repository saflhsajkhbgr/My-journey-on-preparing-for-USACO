
alpha = [i for i in input()]
word = input()

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# word = 'mood'

def solve():
    counter = 0
    pos = 0
    while True:
        counter += 1
        for letter in alpha:
            if word[pos] == letter:
                # print('found', letter, 'in', counter)
                pos += 1
                if pos == len(word):
                    return counter

ans = solve()
print(ans)
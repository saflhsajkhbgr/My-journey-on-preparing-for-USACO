#
# n = int(input())
# string = input()
# """
# GHGHG
# """
# ans = 0
# for i in range(n):
#     countG = 0
#     countH = 0
#     for j in range(i, n):
#         if string[j] == 'G':
#             countG += 1
#         if string[j] == 'H':
#             countH += 1
#         if countG > 1 and countH > 1:
#             break
#         elif countG+countH>=3 and (countH == 1 or countG == 1):
#             # print(string[i:j+1])
#             ans += 1
#
# print(ans)

sets = {[1, 2], [3, 4]}
# sets.append({[3, 4], [1, 2]})
# print(sets)
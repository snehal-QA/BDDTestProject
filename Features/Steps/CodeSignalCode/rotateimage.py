# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# def rotateImage(a):
#     print(a)
#     a.reverse()
#     print(a)
#     for i in range(len(a)):
#         for j in range(i):
#             temp = a[i][j]
#             a[i][j] = a[j][i]
#             a[j][i] = temp
#     return a
# print(rotateImage(a))
#
# a , b = 2,3
# print(a,b)
# a,b=b,a
# print(a,b)
#
# # def areFollowingPatterns(strings, patterns):
# #     a=[strings.index(i) for i in strings]
# #     b=[patterns.index(i) for i in patterns]
# #     if a==b:
# #         return  True
# #     else:
# #         return False
# # s = ["cat", "dog", "dog"]
# # p = ["a", "b", "b"]
# # areFollowingPatterns(s, p)
# #
# #
# # s = ["cat", "dog", "dog"]
# # for i in (s.index(i) for i in s):
# #     print(i)
# #
# # print([s.index(i) for i in s])
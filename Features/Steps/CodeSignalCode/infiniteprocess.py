# # def isInfiniteProcess(a, b):
# #     if(a==b):
# #         return False
# #     else:
# #         while a!=b:
# #             a=a+1;
# #             b=b-1;
# #             if(a==b):
# #                 return False
# #             return True
# #
# # print(isInfiniteProcess(2, 6))
# #
# # s='abcdeafgbsa'
# # for i in s:
# #     print(i + "********" +str(s.index(i)) + "********" +str(s.rindex(i)))
#
# s=str([2,1,3,5,3,2])
# print(s)
# dt={}
# for i in s:
#     if s.index(i) != s.rindex(i):
#         indexdiff = s.rindex(i) - s.index(i)
#         dt[i]= indexdiff
# print(dt)
# print(min(dt.values()))
# print(dt)
# if min(dt.values() == 1):
#     print( -1)
# else:
#     print( dt.values[min(dt.values())])
#
#
#
#
#

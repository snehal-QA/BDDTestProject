# a=[10, 1, 5, 3, 8]
# b=[100, 6, 3, 1, 5]
# v=4
# #Mysolution: Failed due to more execution time
# # def sumOfTwo(a, b, v):
# #     if len(a)>0 and len(b)>0:
# #         for i in a:
# #             for j in b:
# #                 if (i + j == v):
# #                     return True
# #     return False
# # ------------------------------------------------
# #Passed Solution:
# def sumOfTwo(a, b, v):
#     #No need to add if any of two lists are empty
#     if not a or not b:
#         return False
#     #remove duplicates from second array
#     b=set(b)
#     for x in a:
#         if(v-x in a):
#             return True
#     return False
#
# print(sumOfTwo(a,b,v))
#
#
#

# # # You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?
# # # Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.
# # # Example
# # # For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
# # # knapsackLight(value1, weight1, value2, weight2, maxW) = 10.
# # # ou can only carry the first item.
# # # For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
# # # knapsackLight(value1, weight1, value2, weight2, maxW) = 16.
# # # You're strong enough to take both of the items with you.
# # # For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
# # # knapsackLight(value1, weight1, value2, weight2, maxW) = 7.
# # # You can't take both items, but you can take any of them.
# # def knapsackLight(value1, weight1, value2, weight2, maxW):
# #     if(weight1+weight2<=maxW):
# #         return value1+value2
# #     elif(weight1+weight2>maxW):
# #         if (weight1<maxW):
# #             if (weight2 < weight1):
# #                 return value1
# #             else:
# #                 if (weight2 < maxW):
# #                     return value2
# #         elif (weight2 < maxW):
# #             if (weight1 < weight2):
# #                 return value2
# #             else:
# #                 if (weight2 < maxW):
# #                     return value1
# #         else:
# #             return 0
#
# def knapsackLight(value1, weight1, value2, weight2, maxW):
#         if maxW < weight1 and maxW < weight2:
#             return 0
#         elif maxW >= weight1 and maxW < weight2:
#              return value1
#         elif maxW >= weight1 and maxW >= weight2:
#             if maxW >= weight1+weight2:
#                 return value1+value2
#             elif value1 > value2:
#                 return value1
#             else:
#                 return value2
#         elif maxW >= weight2:
#              return value2
#
# print(knapsackLight(4,3,3,4,4))
#
#    # if(weight1+weight2<=maxW):
#     #     return value1+value2
#     # elif(weight1+weight2>maxW):
#     #     if (weight1<maxW):
#     #         if (weight2 < weight1):
#     #             return value1
#     #         else:
#     #             if (weight2 < maxW):
#     #                 return value2
#     #     elif (weight2 < maxW):
#     #         if (weight1 < weight2):
#     #             return value2
#     #         else:
#     #             if (weight2 < maxW):
#     #                 return value1
#     #     else:
#     #         return 0

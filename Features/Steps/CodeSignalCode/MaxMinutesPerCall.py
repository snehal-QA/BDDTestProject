# def phoneCall(min1, min2_10, min11, s):
#     if s < min1:
#         return 0
#     elif s == min1:
#         return 1
#     else:
#         aftermin1= s - min1
#         if aftermin1 < min2_10:
#             return 1
#         elif aftermin1 < min2_10*9:
#             return (1 + int(aftermin1/min2_10))
#         else:
#             aftermin2_10=aftermin1 - min2_10*9
#             if aftermin2_10 < min11:
#                 return (1 + int(aftermin1/(min2_10)))
#             else:
#                 return (10 + int(aftermin2_10/min11))
#
# print(phoneCall(3,1,2,20))
#
#
#
#

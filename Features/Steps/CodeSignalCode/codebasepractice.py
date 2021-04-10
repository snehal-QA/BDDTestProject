# # def addTwoDigits(n):
# #   a=list(str(n))
# #   sum=int(a[0])+int(a[1])
# #   print ("Sum of two digits: "+ str(sum))
# #   return sum
# #
# # addTwoDigits(15)
#
# # def maxMultiple(divisor, bound):
# #     a=divisor*int(bound/divisor)
# #     print(a)
# #     if(a%divisor and a<=bound):
# #         return a
#
# def circleOfNumbers(n, firstNumber):
#     if (firstNumber >= n / 2):
#         return (f1 - int(n / 2))
#     else:
#         return (f1 + int(n / 2))
#
#
# def lateRide(n):
#     hours=int(n/60)
#     minutes=int(n%60)
#
#     t1=list(str(hours))
#     t2=list(str(minutes))
#     t3=t1+t2
#     x=0
#     for i in t3:
#             x=x+int(i)
#     return(x)
#
# #lateRide(880)
#
# def phoneCall(min1, min2_10, min11, s):
#     totalminutes=0
#     centsafterminutecall=0
#     centsafter2_10call=0
#     centsafter11min=0
#     if(s<min1):
#         return 0
#     elif(s == min1):
#         return 1
#     else:
#         totalminutes=1
#         centsafterminutecall=s-min1
#         if(centsafterminutecall<min2_10):
#             return totalminutes
#         # elif(centsafterminutecall==min2_10):
#         #     totalminutes=2
#         #     return totalminutes
#         elif(centsafterminutecall>=min2_10):
#             centsafter2_10call = centsafterminutecall - (9   * min2_10)
#             for x in range(10):
#                 if(centsafter2_10call<min2_10):
#                     totalminutes=totalminutes+1
#                     return totalminutes
#                     break
#                 else:
#                     centsafter2_10call=min2_10-centsafter2_10call
#                     totalminutes=totalminutes+1
#             if(centsafter2_10call>min11):
#                 centsafter11min=min11-centsafter2_10call
#                 if(centsafter11min<min11):
#                     return totalminutes
#                 elif(centsafter11min==min11):
#                     return totalminutes+1
#                 else:
#                     x=0
#                     while(centsafter11min==0 || centsafter11min<min11):
#                         totalminutes=totalminutes+1
#                         return totalminutes
#
# # phoneCall(3, 1, 2, 4)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

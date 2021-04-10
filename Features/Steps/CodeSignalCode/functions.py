# class MethodOperation:
#     a=10
#     __salary=1000
#
#     def __init__(self):
#         print('Class constructor')
#
#     def sum(self,a,b):
#         return(a+b)
#
#     def subtract(self,a,b):
#         return(a-b)
#
# mo=MethodOperation();
# print(mo.a)
# print(MethodOperation.a)
# print('sum is: '+str(mo.sum(10,30)))
# print('Subtraction is: '+str(mo.subtract(30,20)))
# print(mo._MethodOperation__salary)
#
# t1=('sneh','abhi',1,2)
# print(t1)
# l1= [10,10,20,13,14,15]
# s1={(1,2,3),1}
# print(s1)
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x if x != "banana" else "orange" for x in fruits if x != "apple"]
#
# fruits = [10,10,20,13,14,15]
#
# #List comprehenssion
# newlist2 = [x*2 if x%2==0 else x*3 for x in fruits if x > 10 ]
#
# newlist2 = [x*2 for x in fruits if x%2 == 0 ]
# newlist3=[]
# for x in fruits:
#     if x % 2 == 0:
#        newlist3.append(x*2)
#
# print(newlist3)
#
# newlist1=[]
#
# for x in fruits:
#     if x != "banana":
#         newlist1.append(x)
#     else:
#         newlist1.append('orange')
#
# #print(newlist1)
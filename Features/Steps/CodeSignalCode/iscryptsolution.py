# # crypt = ["SEND", "MORE", "MONEY"]
# # solution = [['O', '0'],
# #             ['M', '1'],
# #             ['Y', '2'],
# #             ['E', '5'],
# #             ['N', '6'],
# #             ['D', '7'],
# #             ['R', '8'],
# #             ['S', '9']]
#
#
#
# crypt=["A",
#  "A",
#  "A"]
# solution=[["A","0"]]
#
# def isCryptSolution(crypt, solution):
#     solution=dict(solution)
#     l2=[solution.get(i) for i in list(crypt[1])]
#     l3=[solution.get(i) for i in list(crypt[2])]
#     l1=''.join(map(str, [solution.get(i) for i in list(crypt[0])]))
#     l2=''.join(map(str, [solution.get(i) for i in list(crypt[1])]))
#     l3= ''.join(map(str, [solution.get(i) for i in list(crypt[2])]))
#
#     print(l1)
#     print(l2)
#     print(l3)
#     print(int(l1)+int(l2))
#     #print(l4)
#     if(l1=='0' and l2=='0' and l3=='0'):
#         return True
#     else:
#         if(int(l1)+int(l2)==int(l3)):
#             if( int(l1[0]) != 0 or int(l2[0]) != 0     ):
#                 return  True
#             else:
#                 return  False
#         else:
#             return False
#
# print(isCryptSolution(crypt,solution))
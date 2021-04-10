# matrix=[[0,1,1,2], [0,5,0,0], [2,0,3,3]]
#
# # ZeroCheck=[[0]*len(matrix[0])]* len (matrix)
# ZeroCheck = [1] * (len(matrix) * len(matrix[0]))
# #print(matrix)
# #print(ZeroCheck)
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == 0:
#             # print(matrix[i][j])
#             # print(str(i)+'*********'+str(j))
#             for l in range(i,len(matrix)):
#                 ZeroCheck[l * len(matrix[0]) + j] = 0
#
# mx=[]
# for i in range(len(matrix)) :
#     mx=mx+matrix[i]
# #print(ZeroCheck)
# #print(mx)
# d=[mx[m]*ZeroCheck[m] for m in range(len(mx))]
# print(d)
# print(sum(d))
#            # sum=sum+sum(matrix(i))
#             #matrix(i).index(0)
#             #for j in range
# #print(ZeroCheck)
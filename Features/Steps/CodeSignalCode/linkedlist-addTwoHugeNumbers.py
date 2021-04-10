# #Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
#   def printLN(self):
#     printval = self
#     while printval is not None:
#         print(printval.value)
#         printval = printval.next
#
# LN11=ListNode(123)
# LN12=ListNode(4)
# LN13=ListNode(5)
#
# LN11.next=LN12
# LN12.next=LN13
# LN13.next=None
#
# LN1=ListNode(100)
# LN2=ListNode(100)
# LN3=ListNode(100)
#
#
# LN1.next=LN2
# LN2.next=LN3
# LN3.next=None
#
# LN1.printLN()
# LN11.printLN()
#
# def addTwoHugeNumbers(a, b):
#     l1=[]
#     alen = str(a.value)
#     #print(alen + '***&&&&&'+str(a.value))
#     x=str(a.value)
#     #print(len(x))
#     #print(x)
#     while a is not None:
#         l1=l1.append(a.value)
#         a=a.next
#     l2=[]
#     while b is not None:
#         l2=l2.append(b.value)
#         b=b.next
#     #return int(int(l1)+int(l2))
#
#     rt = str(int(l1) + int(l2))
#     print(rt)
#     ln = []
#     for i in range(0,len(rt),len(alen)):
#         ln.append(int(rt[i:i+len(alen)]))
#     print(ln)
#
#
#
#
#
# print(addTwoHugeNumbers(LN11, LN1))

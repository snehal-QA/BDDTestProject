# #Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
#   def printLN(self):
#       printval = self
#       while printval is not None:
#           print(printval.value)
#           printval = printval.next
#
# LN1=ListNode("MON1")
# LN2=ListNode("MON2")
# LN3=ListNode("MON3")
# LN4=ListNode("MON4")
#
# LN1.next=LN2
# LN2.next=LN3
# LN3.next=LN4
#
#
#
# LN11=ListNode("TON1")
# LN12=ListNode("TON2")
# LN13=ListNode("TON3")
# LN14=ListNode("TON4")
#
# LN4.next=LN11
# LN11.next=LN12
# LN12.next=LN13
# LN13.next=LN14
#
#
#
#
# LN1.printLN()
# #LN11.printLN()
#
# # def isListPalindrome(l):
# #     l.printLN()
# #     printval = l
# #     l1=list()
# #     while printval is not None:
# #         l1.append(printval.value)
# #         printval = printval.next
# #     print(l1)
# #     l2=l1.copy()
# #     l1.reverse()
# #     print(l1)
# #     print(l2)
# #     return l1==l2
# #
# # LN1=ListNode("A")
# # LN2=ListNode("B")
# # LN3=ListNode("C")
# #
# # LN1.next=LN2
# # LN2.next=LN3
# #
# # #l =[0, 1, 0]
# # print(isListPalindrome(LN1))
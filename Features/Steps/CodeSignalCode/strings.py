# list1=[1,2,3]
# #Insert: element to the specific index in list
# list1.insert(2,'snehal')
# print(list1)
#
# # Append: Adds element at the end of the list
# list1.append('abhijit')
# print(list1)
#
# #Extend: Appends two lists use extend function r +  ; extends methods is also use to append iterable collections
# # like tuples,sets,dictionares
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# # thislist.extend(tropical)
# print(thislist+tropical)
#
# #Remove: To remove specified item from list
# veglist=['cabbage','spinach','frenchbeans']
# veglist.remove('cabbage')
# print(veglist)
#
# #pop: To remove from specified Index
# flowerlist=['rose','marigold','jasmine']
# flowerlist.pop(1)
# print(flowerlist)
#
# #Clear list
# l1=['bmw','audi','toyota']
# l1.clear()
# print(l1)
#
# #to delete the list
# l2=['bus','car']
# del l2
# #print(l2)
#
# #----------------------Loops--------------------#
# # 1. To read elements of list
# for x in flowerlist:
#     print(x)
# #2. To loop through index numbers
# for i in range(len(flowerlist)):
#     print(flowerlist[i])
# #3.While loop
# print("while loopstarts here")
# i=0
# while (i<len(flowerlist)):
#     print(flowerlist[i])
#     i=i+1
# else:
#     print("List is complete")
#
# #Loop Comprehension
# translist=['train','bus','tram','yacht','cruise']
# [print(x) for x in translist]
#
# #list Comprehension
# #Accept only numbers lower than 5
# newlist=[]
# for x in range(6):
#     if(x<5 and x>0):
#         newlist.append(x)
# newlist=[x for x in range(6) if(x<5 and x>0)]
# print(newlist)
#
# #Set the values in the new list to upper case:
# newlist1=[x.upper() for x in flowerlist]
# print(newlist1)
#
# ## Sort list : Sort function sorts list
# flowerlist.sort()
# print(flowerlist)
#
#
# #sort the list with numbers close to 50
# thislist=[100,50,65,82,23]
# print('Before sort: '+str(thislist))
# def closestfun(n):
#     print(abs(n-50)+)
#     return abs(n-50)
# thislist.sort(key=closestfun)
# print('After sort: '+str(thislist))
#
#

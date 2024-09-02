#Task1
#a
# for i in range(24,-7,-6):
#     print(i, end= " ")
# print()
# #b
# for i in range(-10,21,5):
#     print(i , end=" ")
# print()
# #c
# for i in range(18,64,9):
#     print(i, end=" ")
# print()
# #d
# for i in range(18,64,9):
#     if i%2==0:
#         print(i, end=" ")
#     else:
#         print(-i,end=" ")
# print()
# [print(i, end=" ") for i in range(-10, 21, 5)]
# print()
# print(" ".join(str(i) for i in range(-10, 21, 5)))

#a=[print(i) for i in range(-10,21,5)]
#print(a)

#Task2
# name=input("Enter a name : ")
# num=int(input("Enter a number : "))
# for i in range(num):
#     print(name)


#Task3
# num=0
# for i in range(601):
#     if i%7==0 and i%9==0:
#         num+=i
# print(num)

#Task4

# num=0
# for i in range(601):
#     if i%7==0 and i%9==0:
#         pass
#     elif i%7==0 or i%9==0:
#         num+=i
# print(num)

#Task5
# num1=int(input("enter a number: "))
# num2=int(input("enter a number: "))
# for i in range(num1,num2+1):
#     if i%2!=0 :
#         print(i ,end=" ")


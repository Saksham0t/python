import math as m
# print("hello world")
# print(4+4)
# num = [5,3,6,55,34,66,99]
# print(num[2])
# print(num[2:5])
# print(num[-1])
# num.append(1)
# print(num)
# print(min(num))
# # List are immutable
# list = [3,5,6,22,'Saksham']
# # tuple is mutable
# tuple = (5,55,'anuj')
# # set doesn't support indexing
# set = {5,2,6,}
#
# names = ['saksham','akshit','abhay']
# values = ['java','c','js']
# combine = dict(zip(names,values))
# print(combine)
# print(id(num))
# print(type(num))
# dic = {'rahul':'samsung', 'vijay':'apple', 'rohan':'oneplus'}
# print(dic)
# print(dic.keys())
# print(dic.values())

# a=5
# b=6
# print(a<7 and b<8)

# print(0b11001)
# print(bin(25))
# print(oct(25))
# print(hex(25))

# a=5
# b=6
# temp = a          #1
# a=b
# b=temp
# print(a)
# print(b)
# a=a+b             #2
# b=a-b
# a=a-b
# print(a)
# print(b)
# a=a^b             #3
# b=a^b
# a=a^b
# print(a)
# print(b)
# a,b=b,a           #4
# print(a)
# print(b)

# print(m.sqrt(25))
# print(m.floor(2.5))
# print(m.ceil(2.5))

# x=int(input("enter first num"))
# y=int(input("enter second num"))
# z=x+y
# print(z)

# n=int(input('enter num:'))
# cube= n**3
# print(cube)

# a = int(input("Enter num:"))
# r = a%2
# if(r==0):
#     print('even')
# else:
#     print('odd')

# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# if(a>b and b>c):
#     print("a is greatest")
# elif(c>b):
#     print("c is greatest")
# else:
#     print("b is greatest")

# i=1
# while(i<5):
#     print("Hello ", end="")
#     j=1
#     while(j<4):
#         print("World ", end="")
#         j=j+1
#     i=i+1
#     print()

# i=1
# while(i<=100):
#     if(i%3!=0 and i%5!=0):
#      print(i)
#     i=i+1

# for i in range(4,9,2):
#     print(i)

# for i in range(4):
#     for j in range(4-i):
#         print("#",end=" ")
#     print()

num=int(input("Enter num: "))
for i in range(2,num):
    if num % 2==0:
        print(num,"is not prime")
        break
else:
    print(num,"is prime")





























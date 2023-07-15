# print("hell")
# x=int(input("Enter x:"))
# y=int(input("Enter y:"))
# z=int(input("Enter z:"))
# print(x+y+z)
# print(x-y)
# print(x*y)
# print(x/y)

# a=int(input("Enter marks of maths:"))
# b=int(input("Enter marks of chemistry:"))
# c=int(input("Enter marks of punjabi:"))
# d=int(input("Enter marks of english:"))
# e=int(input("Enter marks of biology:"))
# total_marks = a+b+c+d+e
# print(total_marks)
# average= (a+b+c+d+e)/5
# print(average)
# percentage = (a+b+c+d+e)/5
# print(percentage)


# length=int(input("Enter length in cm:"))
# meter=length/100
# print(meter)
# km=length/100000
# print(km)

# i = int(input("Enter Number:"))
# rev=0
# x=i
# while i>0:
#     rev= (rev*10)+ i % 10
#     i=i//10
# if(x==rev):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# i = int(input("Enter Number for armstrong:"))
# sum=0
# x=i
# while(i>0):
#     sum= sum+(i%10)*(i%10)*(i%10)
#     i=i//10
# if(sum==x):
#     print("Armstrong")
# else:
#     print("Not")

# def ar(a,b):
#     sum=a+b
#     return sum
# print(ar(2,5))

# def arg(x,y):
#     avg=(x+y)/2
#     return avg
# print(arg(x=7,y=5))
#
# def argu(x)
#     3+;=

# a, b = input("Enter the number : "), input("Enter the number : ")
# sum = float(a) + float(b)
# diff = float(a) - float(b)
# multi = float(a) * float(b)
# div = float(a) / float(b)
# print( a, " + ", b, " = ", sum)
# print( a, " - ", b, " = ", diff)
# print( a, " * ", b, " = ", multi)
# print( a, " / ", b, " = ", div)

# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("The number is not palindrome!")

# num = int(input("Enter a number: "))
# sum = 0
# n1 = len(str(num))
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** n1
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

# dic = {'rahul': 'samsung', 'vijay': 'apple', 'rohan': 'oneplus', 'age':'7'}
# print(dic)
# print(dic['rahul'])
# # print(dic['vijay','rohan'])
# dic['rahul']= 'moto'
# dic['age']='9'
# print(dic)
# tp=()
# tp2=("hello",)
# print(type(tp))
# print(type(tp2))
# tp3=("")

# class Class1:
#     def m(self):
#         print("In Class1")
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
# class Class4(Class2, Class3):
#     pass
# obj = Class4()
# obj.m()

# def reverse(string):
# 	string = string[::-1]
# 	return string
# s = "Geeksforgeeks"
# print("The original string is : ", s)
# # print(s)
# print("The reversed string is : ", reverse(s))
# # print(reverse(s))

# list1 = [1, 2, 1, 1, 4, 5]
# list1.remove(1)
# print(list1)

# my_string = "Hi!? I!? love!? Python!?"
# replacements = [('!', ''), ('?', '')]
# for char, replacement in replacements:
#     if char in my_string:
#         my_string = my_string.replace(char, replacement)
# print(my_string)

# string1 = "Hello There"
# string2 = string1.replace('h', ' ')
# print(string1)
# print(string2)

# li = [1,2,3]
# print(type(li))
# li.reverse()
# print(li)
# li.remove(3)
# print(li)

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)



# class Car:
#     def __init__(self):
#         self.brand="tata"
#         self.color="black"
#     def start(self):
#         print("car is starting")
#         print(self.color)
#         print(self)
# c1=Car()
# print(c1.color)
# print(c1.brand)
# c1.start()
# print(c1)
#
# o/p
# black
# tata
# car is starting
# black
# <__main__.Car object at 0x000001F0B7847770>
# <__main__.Car object at 0x000001F0B7847770>
from ctypes import c_uint32, c_int64

from project2 import choice


#variables
# a=10
# b=10
# c=10
# d=20
# print(a)
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))

#o/p
# 10
# 140735730906520
# 140735730906520
# 140735730906520
# 140735730906840

# a=10
# print(a)
# print(type(a))
#
# b=20.5
# print(b)
# print(type(b))
#
# c="abc"
# print(c)
# print(type(c))

# a=input()
# b=input()
# print(a)
# print(b)
# a=int(input("enter a number"))
# b=int(input("enter another number"))
# c=a+b
# print(c)

# a=int(input("Enter a number:"))
# b=int(input("Enter another number:"))
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else:
#     print("a is equal to b")

# for i in 1,2,3,4:
#     print(i)
# for i in 10,15.8,"abc":
#     print(i)
# for i in "abc","xyz":
#     print(i)
# for i in "rahul":
#     print(i)
# for i in 10:
#     print(i)

# for i in range(100):
#     print(i)
# for i in range(1,100):
#     print(i)
# for i in range(1,100,2):
#     print(i)
# for i in range(2,100,2):
#     print(i)

# while loop
# i=0
# while i<=2:
#     print("hello")
#     i=i+1

# class student:
#     def __init__(self,name,age,usn):
#         self.sname=name
#         self.sage=age
#         self.susn=usn
# s1=student("abc",22,403)
# s2=student("xyz",22,475)
# print(s1.sname)
# print(s2.susn)
# print(s1.sage)
# print(s2.sage)


# class chair:
#     def __init__(self):
#         self.brand="abc"
#         self.color="brown"
#     def rotate(self):
#         self.cost=700
#         print(self.cost)
# c1=chair()
# print(c1.brand)
# print(c1.color)
# # print(c1.cost)
# c1.rotate()
# print(c1.cost)

# class Farmer:
#     def __init__(self,p,t,r):
#         self.principle=p
#         self.time=t
#         self.rate=r
#     def loan(self):
#         si=(self.principle*self.time*self.rate)/100
#         print(si)
# f1=Farmer(200000,2,2.5)
# f2=Farmer(400000,3,2.5)
# f1.loan()
# f2.loan()

# class Farmer:
#     r=2.5
#     def __init__(self,p,t):
#         self.principle=p
#         self.time=t
#     def loan(self):
#         si=(self.principle*self.time*Farmer.r)/100
#         print(si)
# f1=Farmer(200000,7)
# f2=Farmer(500000,4)
# f1.loan()
# f2.loan()
# print(Farmer.r)

# no parameter no return value
# class calculator:
#     def __init__(self):
#         self.color="black"
#         self.brand="casio"
#     def add(self):
#         a=10
#         b=20
#         c=a+b
#         print(c)
# c1=calculator()
# print(c1.color)
# print(c1.brand)
# c1.add()





#methods in pythonn
# class mobile:
#     def __init__(self):
#         self.brand="Nokia"
#     def call(self):                     #instance method
#         print("mobile call")
#     @staticmethod
#     def charge():
#         print("mobile charge")
#     @classmethod
#     def email(cls):
#         print("mobile email")
# m1=mobile()
# print(m1.brand)
# m1.call()
# m1.charge()
# m1.email()
# mobile.charge()
# mobile.email()


# class calsi:
#     def operators(self,a,b):
#         c1=a+b
#         c2=a-b
#         c3=a*b
#         c4=a/b
#         return c1,c2,c3,c4
# c=calsi()
# r1,r2,r3,r4=c.operators(5,2)
# print(r1)
# print(r2)
# print(r3)
# print(r4)

# class demo:
#     def disp(self,a=10,b=20,c=30):
#         print(a)
#         print(b)
#         print(c)
# d1=demo()
# x=11
# y=22
# z=33
# d1.disp() #crt
# d1.disp(x,y,z) #crt
# d1.disp(x) #crt
# d1.disp(z) #crt
# d1.disp(y,z) #crt
# d1.disp(b=z,a=y,c=x) #crt
# d1.disp(c=y) #crt

# str="sita"
# print(str)
# for i in str:
#     #print(i)
#     print(i,end="")

# str="babu"
# print(str)
# print(len(str))
# print(str[1])
# print(str[-1])
# print(str[-2])


# str1="arju"
# str2="anju"
# str3=str1+str2
# print(str3)
# str4=str1-str2
# print(str4) #TypeError: unsupported operand type(s) for -: 'str' and 'str'
# str5=str1*str2
# print(str5) can't multiply sequence by non-int of type 'str'

# str6=str1*2
# print(str6)
# str7=str1/str2
# print(str7) # unsupported operand type(s) for /: 'str' and 'str'

# str1="Loki"
# str2="john"
# str3="Loki"
# str4="shaky"
# str5="loki"
# str6="rahul"
# print(id(str1))
# print(id(str3))
# print(id(str5))
# print(id(str4))

# str="RajaRamMohanRoy"
# print(str[-2:-6])
# print(str[1:8:2])
# print(str[-2:-7:-1])
# print(str[-2:-12:-3])
# print(str[-11:12])
# print(str[-13:-2])
# print(str[11:7:-1])
# print(str[: :])
# # print(str[::2])
# print(str[::-4])
# print(str[1:9:-2])
# print(str[5:-2])
# print(str[::-1])
# print(str[1:8:0]) # slice step cannot be zero]


# str=" rahul is driking "
# print(str)
# str1=str.lstrip()
# print(str1)
# str2=str.rstrip()
# print(str2)
# str3=str.strip()
# print(str3)

# str="u m a"
# print(str)
# str1=""
# for i in str:
#     if i == " ":
#         pass
#     else:
#         str1=str1+i
# print(str1)

# str=input("enter string")
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)

# str="guru is drinking"
# str1=str.split()
# print(str)
# print(str1)

# str="guru is drinking"
# str1=str.split()
# rev=""
# for i in str1:
#     rev=i+rev
# print(rev)

# str=input("enter sentence")
# str1=str.split()
# rev=""
# for i in str1:
#     rev=i+" "+rev
# print(rev)

# str=input("enter string")
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)
# if str==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#
# str=input("enter string")
# print(str)
# if str.isalpha():
#     print("str contains only alphanumeric characters")
# elif str.isdigit():
#     print("str contains only digits")
# elif str.isalnum():
#     print("contains both")
# else:
#     print("other char")
#
# str=input("enter string")
# print(str)
# str1=str.upper()
# print(str1)
# str2=str.lower()
# print(str2)
# str3=str.swapcase()
# print(str3)

# text = input("Enter string: ")
# print(text)
#
# str1 = text.upper()
# print(str1)
#
# str2 = text.lower()
# print(str2)
#
# str3 = text.swapcase()
# print(str3)


# str="if you think you can or you can't , you are right"
# print(str)
# str1="you"
# print(str1 in str)
# print(str.index("you"))
# print(str.find("you"))
# print(str.rindex("you"))
# print(str.rfind("you"))
# print(str.find("python"))
# print(str.index("python")) #throw an error

#FUNCTIONS
# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# add()


# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# add()
#
# def add():
#     a=10
#     b=20
#     c=a+b
#     return c
# add()
# res=add()
# print(res)
#
# def add(a,b):
#     c=a+b
#     print(c)
# x=10
# y=20
# add(x,y)
#
# def add(a,b):
#     c=a+b
#     return c
# x=10
# y=20
# res=add(x,y)
# print(res)

# def fun1():
#     print("inside fun1")
# def fun2():
#     print("inside fun2")
# ptr1=fun1
# ptr2=fun2
# ptr1()
# ptr2()

# alpha=input("enter a alpha")
# res=ord(alpha)
# print(res)
#
# num=int(input("enter a number"))
# res1=chr(num)
# print(res1)


# def outer():
#     print("inside outer")
#     def inner():
#         print("inside inner")
#     inner()
# outer()

# def fun1():
#     print("inside fun1")
# def fun2(ptr):
#     print("entering fun2")
#     ptr()
#     print("leaving fun2")
# fun1()
# fun2(fun1)


# a=10
# def fun1():
#     a=100
#     b=200
#     print(a)
#     print(b)
# def fun2():
#     c=500
#     print(a)
#     print(c)
# fun1()
# fun2()


# a=100
# def fun1():
#     global a
#     a=10
#     b=20
#     print(a)
#     print(b)
# def fun2():
#     global a
#     a=15
#     b=25
#     print(a)
#     print(b)
# print(a)
# fun1()
# print(a)
# fun2()
# print(a)

# def outer():
#     a=100
#     b=200
#     print(a)
#     print(b)
#     def inner():
#         nonlocal a
#         a=150
#         b=250
#         print(a)
#         print(b)
#     print(a)
#     inner()
#     print(a)
# outer()


# def square(num):
#     return num * num
# lambda num : num * num
# l=lambda num : num * num
# res=l(5)
# print(res)
#
# def add(a,b):
#     return a+b
# lambda a,b: a+b
# res=add(5,6)
# print(res)


# def outer():
#     a=10
#     b=20
#     print(a)
#     print(b)
#     def inner():
#         c=15
#         print(a)
#         print(c)
#     inner()
# outer()

# def outer():
#     a=100
#     print(a)
#     print(b)
#     def inner():
#         b=200
#         print(b)
#     inner()
# outer()

# LEGB rule
# a=10
# def outer():
#     a=15
#     def inner():
#         a=20  #local scope
#         print(a)
#     inner()
# outer()
#
# a=10
# def outer():
#     a=15 #enclosed scope
#     def inner():
#         # a=20
#         print(a)
#     inner()
# outer()
#
#
# a=10 #global scope
# def outer():
#     # a=15
#     def inner():
#         # a=20
#         print(a)
#     inner()
# outer()

# built in scope
# from math import pi
# # pi=10
# def outer():
#     # pi=15
#     def inner():
#          # pi=20
#         print(pi)
#     inner()
# outer()


# closure imp for interview
# def outer():
#     print("inside outer")
#     def inner():
#         print("inside inner")
#     return inner
# ref=outer()
# ref()


# program to collect 5 interger value from the user

# L = []
# i=0
# while i<=4:
#     num=int(input("enter a number"))
#     L.insert(i,num)
#     i=i+1
# print(L)
#
#
# i=0
# while i<=4:
#     print(L[i])
#     i=i+1

# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# L=[]
# i=0
# while i<=4:
#     num=int(input("Enter a number: "))
#     L.insert(i,num)
#     i=i+1
# print(L)
# i=0
# while i<=4:
#     data=L[i]
#     choice=even(data)
#     if choice==True:
#         print(L[i])
#     i=i+1

#
# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# L=[]
# i=0
# while i<=4:
#     num=int(input("Enter a number"))
#     L.insert(i,num)
#     i=i+1
# print(L)
# i=0
# while i<=4:
#     data=L[i]
#     choice=even(data)
#     if choice==True:
#         print(L[i])
#     i=i+1


# def generator():
#     yield 1
#     yield 2
#     yield 3
# res=generator()
# print(res)












# def largest_value(l):
#     l=list(set(l))
#     l.sort()
#     return l[-1]
# l=eval(input("enter a list"))
# print(largest_value(l))
from operator import truediv


# --------------->wap to print the second largest element in the given list
# def sec_largest(l):
#     l=list(set(l)) #sets removes duplicate values here
#     l.sort()
#     return l[-2]
# l=eval(input("Enter a list: "))
# print(sec_largest(l))

#------------------>wap merge two list without using + operator
# def merge_list(l1,l2):
#     out=l1
#     for i in l2:
#         out.append(i)
#     return out
# l1=eval(input("enter first list1"))
# l2=eval(input("enter second list2"))
# print(merge_list(l1,l2))


#----------------->wap to find the sum of interger present in a guven a list
# def sum_int(l):
#     sum=0
#     for i in l:
#         if type(i)==int:
#             sum=sum+i
#     return sum
# l=eval(input("enter the list"))
# print(sum_int(l))


#------------------->wap to reverse he list using two pointer
# def rev_list(l):
#     i=0
#     j=len(l)-1
#     while i<j:
#         l[i],l[j]=l[j],l[i]
#         i=i+1
#         j=j-1
#     return l
# l=eval(input("enter a list"))
# print(rev_list(l))

#----------------------->wap to check wether the list is palidrome or not using two pointer
# def palindrome(l):
#     i=0
#     j=len(l)-1
#     flag=True
#     while i<j:
#         if l[i]!=l[j]:
#             flag=False
#             break
#         i=i+1
#         j=j-1
#     if flag:
#         return 'Palindrome'
#     else:
#         return 'Not Palindrome'
# l=eval(input("Enter a list: "))
# print(palindrome(l))


#------------------------>wap to find commom elements from the two lists

# def common_val(l1,l2):
#     out=[]
#     for i in l1:
#         if i in l2 and i not in out:
#             out.append(i)
#     return out
# l1=eval(input("enter first list"))
# l2=eval(input("enter second list"))
# print(common_val(l1,l2))

#------------------------->wap to find frequesncy of elements from the given list
# def freq_element(l):
#     out=[]
#     for i in l:
#         if i not in out:
#             print(i,':',l.count(i))
#             out.append(i)
# l=eval(input("enter the element:"))
# freq_element(l)

#--------------->wap to rotate the list for n number of times to right or left
#

#---------> o/p:enter a list[5,7,8,9]
# enter a number2
# [8, 9, 5, 7]

# left rotation
# def left_rotate(l,n):
#     n=n%len(l)
#     out=l[n:]+l[:n]
#     return out
# l=eval(input("enter a list"))
# n=int(input("enter a number"))
# print(left_rotate(l,n))

#-------------->o/p:enter a list[1,2,3,4,5]
# enter a number3
# [4, 5, 1, 2, 3]

#------------------>wap to move zeros to end of the list
# def move_zero(l):
#     zero=[]
#     out=[]
#     for i in l:
#         if i!=0:
#             out.append(i)
#         else:
#             zero.append(i)
#     return out+zero
# l=eval(input("Enter a list: "))
# print(move_zero(l))

# o/p:Enter a list: [1,0,5,7,0,8]
# [1, 5, 7, 8, 0, 0]

# -------------->wap to find missing number from list(1 to n)
# n*(n+1)//2 flow division
# def missing_num(l):
#     n=int(input("enter n value"))
#     sum_val=sum(l)
#     res=n*(n+1)//2
#     return res-sum_val
# l=eval(input("enter list"))
# print(missing_num(l))  #applicable only when single value is missing
# o/p:enter list[1,2,3,5]
# enter n value5
# 4

#------------->applicable for multiple values missing
# def missing_num(l):
#     n=int(input("enter n value"))
#     sum_val=sum(l)
#     res=n*(n+1)//2
#     return res-sum_val
# l=eval(input("enter list"))
# n=int(input("enter val"))
# for i in range(1,n+1):
#     if i not in l:
#         print(i)
# o/p:enter list[1,2,4,5,7]
# enter val7
# 3
# 6


#---------------->wap to find the pair with given sum
# def sam(l, n):
#     out = []
#     for i in range(len(l)):
#         if l[i] == n:
#             out.append([l[i]])
#         else:
#             for j in range(i + 1, len(l)):
#                 if l[i] + l[j] == n:
#                     out.append([l[i], l[j]])
#     return out
#
# l = eval(input("Enter the list: "))
# n = int(input("Enter n value: "))
# print(sam(l, n))
# o/p:Enter the list: [1000,700,100,300,900,200]
# Enter n value: 1000
# [[1000], [700, 300], [100, 900]]


#string
#reverse a string
# def rev_str(s):
#     l=list(s)
#     i=0
#     j=len(l)-1
#     while i<j:
#         l[i],l[j]=l[j],l[i]
#         i=i+1
#         j=j-1
#     return "".join(l)
# s=input("enter a string")
# print(rev_str(s))

#check palindrome

# def palindrome(s):
#     i = 0
#     j = len(s) - 1
#     flag = True
#
#     while i < j:
#         if s[i] != s[j]:
#             flag = False
#             break
#         i = i + 1
#         j = j - 1
#
#     if flag:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"
#
#
# s = input("Enter a string: ")
# print(palindrome(s))

#count of vowels nd consonents in given string
# def count_vow_con(s):
#     vow=0
#     cons=0
#     for i in s:
#         if i in "AEIOUaeiou":
#             vow = vow+1
#         elif 'A' <= i <= 'Z'or 'a' <= i <= 'z':
#             cons = cons+1
#     return vow,cons
# s=input("Enter a string: ")
# print(count_vow_con(s))
# Enter a string: hai
# (2, 1)

#wap to count occurrence of element in given string
# def occur_element(s):
#     count=0
#     element=input("enter element: ")
#     for i in s:
#         if i==element:
#             count = count+1
#     return count
# s=input("Enter a string: ")
# print(occur_element(s))
# o/p: Enter a string: program
# enter element: r
# 2


##to print occrence if substring from given string
# def occur_substr(s,sub):
#     count=0
#     for i in range(len(s)-len(sub)+1):
#         if s[i:i+len(sub)]==sub:
#             count = count+1
#     return count
# S=input("Enter a string: ")
# sub=input("Enter a substring: ")
# print(occur_substr(S,sub))
# o/p:Enter a string: malayalam
# Enter a substring: la
# 2


#remove spaces from a given string
# def rem_spac(s):
#     res=""
#     for i in s:
#         if i!=" ":
#             res=res+i
#     return res
# s=input("Enter a string: ")
# print(rem_spac(s))
# Enter a string: h a i
# hai



# 3rd cls
# wap to check the rotation of the string
# def rotation_str(s1,s2):
#     if len(s1) == len(s2) and s2 in (s1+s2):
#         print("rotation of string")
#     else:
#         print("rotation failed")
# s1=input("enter first string")
# s2=input("enter second string")
# rotation_str(s1,s2)
# o/p:
# enter first stringhello
# enter second stringllohe
# rotation of string


# wap to insert the substring into the main string from the given index number
# def add_substr(s,sub,ind):
#     if ind<0 or ind>len(s):
#         return "invalid index"
#     else:
#         new_str=s[:ind]+sub+s[ind:]
#         return new_str
# s=input("enter string")
# sub=input("enter substring")
# ind=int(input("enter index"))
# print(add_substr(s,sub,ind))
#
# o/p:
# enter stringprogramming
# enter substringm
# enter index6
# programmming


#wpa to print largest palindrome substring from the given string
# def large_pali_sub(s):
#     large=""
#     for i in range(len(s)):
#         for j in range(i+1,len(s)+1):
#             sub=s[i:j]
#             if sub == sub[::-1] and len(sub)>len(large):
#                 large=sub
#     return large
# s=input("enter string")
# print(large_pali_sub(s))
#
# o/p:
# enter stringabad
# aba


#--------------------->NUMBER
#wap to check whether the given number is prime number or not
# def prime_num(n):
#     count=0
#     for i in range(1,n+1):
#         if n % i == 0:
#             count = count + 1
#     if count == 2:
#         return "prime number"
#     else:
#         return "not prime"
# n=int(input("enter the number"))
# print(prime_num(n))
# o/p:enter the number8
# not prime


#wap to reverse the number
# def rev_num(n):
#     rev=0
#     while n>0:
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     return rev
# n=int(input("enter the number"))
# print(rev_num(n))
# o/p:
# enter the number45
# 54

#wap to check whether given number is palindrome or not
# def palindrome(n):
#     rev=0
#     temp=n
#     while temp>0:
#         ld=temp%10
#         rev=rev*10+ld
#         temp=temp//10
#     if n ==rev:
#         return "palindrome"
#     else:
#         return "not palindrome"
# n=int(input("enter the number"))
# print(palindrome(n))
# o/p:
# enter the number12
# not palindrome


#wap to check whether the given number is armstrong or not
# def armstrong_num(n):
#     sum=0
#     for i in str(n):
#         num=int(i)
#         sum=sum+num**len(str(n))
#     if sum==n:
#         return "armstrong number"
#     else:
#         return "not armstrong number"
# n=int(input("enter the number"))
# print(armstrong_num(n))
# o/p:
# enter the number153
# armstrong number

#wap to check whether the given number is strong number or not
# def strong_num(n):
#     sum=0
#     for i in str(n):
#         num=int(i)
#         fact=1
#         for j in range(1,num+1):
#             fact=fact*j
#         sum=sum+fact
#     if sum==n:
#         return "strong number"
#     else:
#         return "not strong number"
# n=int(input("enter the number"))
# print(strong_num(n))
# o/p:
# enter the number145
# strong number


#wap to check whether given number is perfect number or not
# def perfect_num(n):
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum = sum + i
#
#     if sum == n:
#         return "perfect number"
#     else:
#         return "not perfect number"
#
# n = int(input("enter val: "))
# print(perfect_num(n))
# o/p:
# enter val: 6
# perfect number



# 08-06
# dictionary
#wap to count frequency of character from the string using dictionary
# s=input("enter string:")
# out={}
# for i in s:
#     out[i]=s.count(i)
# print(out)

#wap to merge two dictionary
# d1=eval(input("enter dictionary:"))
# d2=eval(input("enter dictionary:"))
# d1.update(d2)
# print(d1)

# 2nd way------->
# d1=eval(input("enter dictionary:"))
# d2=eval(input("enter dictionary:"))
# out=d1
# for i in d2:
#     out[i]=d2[i]
# print(out)


#wap to sort dictionary by values
# d=eval(input("enter the dictionary"))
# items=list(d.items())
# for passno in range(1,len(items)):
#     for i in range(len(items)-passno):
#         if items[i][1] > items[i+1][1]:
#             items[i],items[i+1]=items[i+1],items[i]
# out={}
# for k,v in items:
#     out[k]=v
# print(out)
# o/p:
# enter the dictionary{'a':10,'b':5,'c':20}
# {'b': 5, 'a': 10, 'c': 20}

#wap to map two list into dictionary
# l1=eval(input("enter the dict"))
# l2=eval(input("enter the dict"))
# d={}
# for i in range(0,len(l1)):
#     d[l1[i]]=l2[i]
# print(d)

#pattern
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()
# o/p:
# *
# **
# ***
# ****
# *****

# n=5
# for i in range(1,n+1):
#     for space in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,n-i+2):
#         print("*",end=" ")
#     print()
# o/p:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# n=5
# for i in range(1,n+1):
#     for space in range(i,1):
#         print("",end=" ")
#     for j in range(1,n-i+2):
#         print("*", end=" ")
#     print()
# # o/p;
# * * * * *
# * * * *
# * * *
# * *
# *


# n=5
# for i in range(1,n+1):
#     for space in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()
# o/p:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *


# recombination pattern:
# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print("*",end=" ")
#     for space in range(1,i):
#         print(" ",end=" ")
#     for sp in range(1,i):
#         print(" ",end=" ")
#     for k in range(1,n-i+2):
#         print("*",end=" ")
#     print()
# o/p:
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     for space in range(1,n-i+1):
#         print(' ',end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
# o/p:
# *         *
# * *       * *
# * * *     * * *
# * * * *   * * * *
# * * * * * * * * * *


# n=4
# for i in range(1,n+1):
#     for space in range(1,n-i+1):
#         print(' ',end='')
#     for j in range(1,i+1):
#         print('*',end='')
#     for k in range(1,i):
#         print('*',end='')
#     print()
# o/p:
#    *
#   ***
#  *****
# *******


# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()
# n=3
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print('*',end=' ')
#     print()
#
# o/p:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

#
# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print('*',end=' ')
#     for space in range(1,i):
#         print(' ',end=' ')
#     for sp in range(1,i):
#         print(' ',end=' ')
#     for k in range(1,n-i+2):
#         print('*',end=' ')
#     print()
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     for space in range(1,n-i+1):
#         print(' ',end=' ')
#     for sp in range(1,n-i+1):
#         print(' ',end=' ')
#     for k in range(1,i+1):
#         print('*',end=' ')
#     print()
# o/p:
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
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


# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# L=[]
# i=0
# while i<=4:
#     num=int(input("Enter a number:"))
#     L.insert(i,num)
#     i=i+1
# print(L)
# res=list(filter(even,L))
# print(res)

# L=[]
# i=0
# while i<=4:
#     num=int(input("Enter a number:"))
#     L.insert(i,num)
#     i=i+1
# print(L)
# res=list(filter(lambda num: num%2==0,L))
# print(res)


# def add(num):
#     return num+10
# L=[]
# i=0
# while i<=4:
#     num=int(input("Enter a number:"))
#     L.append(num)
#     i=i+1
# print(L)
# res=list(map(add,L))
# print(res)


# L=[]
# i=0
# while i<=4:
#     num=int(input("Enter a number:"))
#     L.append(num)
#     i=i+1
# print(L)
# res=list(map(lambda num:num+10,L))
# print(res)

#
# def main():
#     print("inside main")
# def outer(ptr):
#     print("inside outer")
#     def inner():
#         print("inside inner")
#         ptr()
#         print("leavinf inner")
#     return inner
# ref=outer(main)
# ref()

# def main():
#     str="pentagon"
#     return str
# def outer(ptr):
#     print("inside outer")
#     def inner():
#         print("entering inner")
#         res=ptr()
#         ans=res.upper()
#         print(ans)
#         print("leaving inner")
#     return inner
# ref=outer(main)
# ref()



